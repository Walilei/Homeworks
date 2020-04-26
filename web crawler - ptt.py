import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/M.1587888439.A.E83.html'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')


content = soup.find('div', {'id':'main-content'}).text.split('※')[0]
info = []
for i in soup.find_all('span', {'class':'article-meta-value'}):
    info.append(i.text)
author = info[0]
title = info[2]
time = info[3]

like = 0
dislike = 0
score = like - dislike
for i in soup.find_all('div', {'class':'push'}):
    if i.text[0] == '推':
        like += 1
    elif i.text[0] == '噓':
        dislike += 1

print(content.strip('\n').strip('--'))
print('--我是分隔線--')
print(f"推： {like}")
print(f"噓： {dislike}")
print(f"分數： {score}")
print(f"作者： {author}")
print(f"標題： {title}")
print(f"時間： {time}")
