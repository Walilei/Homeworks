import requests
from bs4 import BeautifulSoup
import json
import pymysql


# 建立函式儲存搜尋到的職務
def store_job(job_url):
    job_idx = job_url[27:32]
    job_json = f'https://www.104.com.tw/job/ajax/content/{job_idx}'
    job_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
                   'Referer': job_url}
    job_req = requests.get(job_json, headers=job_headers)
    job_soup = BeautifulSoup(job_req.text, 'lxml')
    json_file = job_soup.find('p').text
    json_file = json.loads(json_file)

    jobName = json_file['data']['header']['jobName'].replace('"', '_')
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

    # 將職務條件存入已建立的MySQL資料庫
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='*****', db='py_crawler')
    cursor = db.cursor()
    sql = f'''insert into job(id, jobName, comName, appearDate, salary, salaryMin, salaryMax, industry) \
    values("{job_idx}", "{jobName}", "{comName}", "{appearDate}", "{salary}", {salaryMin}, {salaryMax}, "{industry}")\
    ON DUPLICATE KEY UPDATE appearDate = "{appearDate}";
    '''
    cursor.execute(sql)
    db.commit()
    db.close()
    print(f'{jobName} saved!')


'''
建立MySQL資料庫指令
create database py_crawler;
use py_crawler;
create table job (id varchar(5) primary key, jobName varchar(255), comName varchar(255), 
appearDate date, salary varchar(255), salaryMin int, salaryMax int, industry varchar(100));
'''
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
# 104僅提供150頁的資料
for page in range(1, 151):
    # 只取台北地區、大學學歷、需要軟體技術相關資料
    url = 'https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000%2C2004001010%2C2003002002&area=6001001000&' \
          f'edu=4&order=12&asc=0&excludeJobKeyword=%E5%AF%A6%E7%BF%92&page={page}&mode=s&jobsource=2018indexpoc'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    for _ in soup.find_all('div', {'class': 'b-block__left'}):
        job_date = _.find('span', {'class': 'b-tit__date'}).text.replace('\n', '').strip()
        if len(job_date) > 0 and ('//tutor.104.com.tw/' not in _.find('a', {'class': 'js-job-link'})['href']):
            new_url = 'https:' + _.find('a', {'class': 'js-job-link'})['href']
            try:
                new_url = 'https:' + _.find('a', {'class': 'js-job-link'})['href']
                store_job(new_url)
            except json.decoder.JSONDecodeError:
                continue
    print(f'Page {page}')
