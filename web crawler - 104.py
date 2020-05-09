import requests
from datetime import date
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
# 找當天更新的資料
today = f'{date.today().month}/{date.today().day:02}'
page = 1

while page < 10:
    # 只取台北地區、大學學歷以上資料
    url = f'https://www.104.com.tw/jobs/search/?ro=0&isnew=7&area=6001001000&edu=4&order=11&asc=0&' \
          f'page={page}&mode=s&jobsource=2018indexpoc'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    for _ in soup.find_all('div', {'class': 'b-block__left'}):
        job_date = _.find('span', {'class': 'b-tit__date'}).text.replace('\n', '').strip()
        if job_date == today:
            job_title = _.find('a', {'class': 'js-job-link'}).text
            job_url = 'https:' + _.find('a', {'class': 'js-job-link'})['href']
            print(job_title, job_url)
    page += 1
