import requests
from bs4 import BeautifulSoup
req = requests.get('https://movies.yahoo.com.tw/movieinfo_main/%E7%8A%AC%E9%B3%B4%E6%9D%91-howling-village-10543')
html = req.content.decode('utf8')
soup = BeautifulSoup(html, 'lxml')

c_title = soup.find('h1').string
e_title = soup.select_one('h3').string
genre = []
for tag in soup.find_all('a'):
    if 'data-ga' in tag.attrs:
        if '電影介紹_類型icon' in tag['data-ga']:
            str = tag['data-ga'].strip('[').strip(']').split(',')
            genre.append(str[2].strip('\''))

crews = soup.find_all('div', {'class': 'movie_intro_list'})
director = crews[0].text.strip()
actors = crews[1].text.replace(' ', '').replace('\n', '').split('、')

for tag in soup.find_all('span'):
    if '：' in tag.text:
        tag = tag.text.split('：')
        if '上映日期' in tag:
            date = tag[1]
        elif '片　　長' in tag:
            time = tag[1]
        elif '發行公司' in tag:
            com = tag[1]
        elif 'IMDb分數' in tag:
            imdb = tag[1]

story = soup.find('span', {'id': 'story'}).text.strip()

print(f"電影名稱(中英)：{c_title}, {e_title}")
print(f"上映日期：{date}")
print(f"類 型：{', '.join(genre)}")
print(f"片 長：{time}")
print(f"導 演：{director}")
print(f"演 員：{', '.join(actors)}")
print(f"發行公司：{com}")
print(f"劇情介紹：")
print(story)
