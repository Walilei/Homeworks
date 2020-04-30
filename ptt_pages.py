import requests
from bs4 import BeautifulSoup
from ptt_web_crawler import ptt_to_txt

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
cookies = {'over18':'1'}

page = 8932
url = f'https://www.ptt.cc/bbs/movie/index{page}.html'
req = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(req.text, 'html.parser')

while page > 8930:
    for tag in soup.find_all('div', {'class': 'title'}):
        web = 'https://www.ptt.cc/' + tag.find('a')['href']
        res = requests.get(web, headers=headers, cookies=cookies)
        article_soup = BeautifulSoup(res.text, 'html.parser')
        ptt_to_txt(article_soup)
    page -= 1
   
