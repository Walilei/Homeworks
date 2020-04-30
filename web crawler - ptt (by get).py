import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
cookies = {'over18':'1'}
url = 'https://www.ptt.cc/bbs/Gossiping/M.1587950959.A.0F8.html'
req = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(req.text, 'html.parser')

content = soup.find('div', {'id': 'main-content'}).text.split('※ 發信站')[0]
info = []
for i in soup.find_all('span', {'class': 'article-meta-value'}):
    info.append(i.text)
author = info[0]
title = info[2]
time = info[3]

like = 0
dislike = 0
for i in soup.find_all('div', {'class': 'push'}):
    if i.text[0] == '推':
        like += 1
    elif i.text[0] == '噓':
        dislike += 1
score = like - dislike

print(content.strip('\n').strip('--'))
print('--我是分隔線--')
print(f"推： {like}")
print(f"噓： {dislike}")
print(f"分數： {score}")
print(f"作者： {author}")
print(f"標題： {title}")
print(f"時間： {time}")