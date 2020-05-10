import requests
from datetime import date
from bs4 import BeautifulSoup
import json
import pymysql

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
today = f'{date.today().month}/{date.today().day:02}'
page = 1


# 利用函式儲存搜尋到的職務
def store_job(job_url):
    job_idx = job_url[27:32]
    job_json = f'https://www.104.com.tw/job/ajax/content/{job_idx}'
    job_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
                   'Referer': job_url}
    job_req = requests.get(job_json, headers=job_headers)
    job_soup = BeautifulSoup(job_req.text, 'lxml')
    json_file = job_soup.find('p').string
    json_file = json.loads(json_file)

    jobName = json_file['data']['header']['jobName']
    comName = json_file['data']['header']['custName']
    appearDate = json_file['data']['header']['appearDate']
    salary = json_file['data']['jobDetail']['salary']
    salaryMin = json_file['data']['jobDetail']['salaryMin']
    salaryMax = json_file['data']['jobDetail']['salaryMax']
    industry = json_file['data']['industry']
    # specialty = json_file['data']['condition']['specialty']
    # needEmp = json_file['data']['jobDetail']['needEmp']
    # jobCategory = json_file['data']['jobDetail']['jobCategory']

    # 把此職務存成JSON檔案
    # with open(jobName, 'w') as f:
    #     json.dump(json_file, f)

    # 將職務條件存入MySQL資料庫
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='70794', db='py_crawler')
    cursor = db.cursor()
    sql = f'''insert into job(jobName, comName, appearDate, salary, salaryMin, salaryMax, industry) \
    values('{jobName}', '{comName}', '{appearDate}', '{salary}', {salaryMin}, {salaryMax}, '{industry}');
    '''
    cursor.execute(sql)
    db.commit()
    db.close()
    print('file saved!')


while page < 10:
    # 只取台北地區、大學學歷以上資料
    url = f'https://www.104.com.tw/jobs/search/?ro=0&isnew=7&area=6001001000&edu=4&order=11&asc=0&' \
          f'page={page}&mode=s&jobsource=2018indexpoc'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    for _ in soup.find_all('div', {'class': 'b-block__left'}):
        # 只找當天更新的資料
        job_date = _.find('span', {'class': 'b-tit__date'}).text.replace('\n', '').strip()
        if job_date == today:
            # job_title = _.find('a', {'class': 'js-job-link'}).text
            new_url = 'https:' + _.find('a', {'class': 'js-job-link'})['href']
            store_job(new_url)
    page += 1
