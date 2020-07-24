import feedparser
import requests
from bs4 import BeautifulSoup
import jieba
from http import cookiejar

rss_url = "https://money.udn.com/rssfeed/news/1001/5588/5599?ch=money"
newsFeed = feedparser.parse(rss_url)

# import json
# newsFeed['bozo_exception'] = 'document declared as us-ascii, but parsed as utf-8'
# print(json.dumps(newsFeed))

jieba.set_dictionary('dict.txt.big')
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
my_headers = {
    'User-Agent': user_agent,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "cache-control": "no-cache",
    "Accept-Charset": "UTF8,utf-8;q=0.7,*;q=0.7"
}
my_cookie = cookiejar.CookieJar()

filter_text = []
for e in newsFeed['entries']:
    url = e['links'][0]['href']
    r = requests.get(url, headers = my_headers, cookies = my_cookie).text
    soup = BeautifulSoup(r, 'lxml')
    article = soup.find('div', {'id': 'article_body'})
    article_lines = []
    for paragraph in article.find_all('p'):
        if '點我領取' not in paragraph.text:
            article_lines.append(paragraph.text.replace('\n', '').replace('\r', ''))
    article_text = ''.join(article_lines)
    seg_words_list = jieba.lcut(article_text)

    with open(file='stop_words.txt', mode='r', encoding='utf-8') as file:
        stop_words = file.read().split('\n')
        for term in seg_words_list:
            if term not in stop_words:
                filter_text.append(term)

import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

seg_words = ' '.join(filter_text)
wordcloud = WordCloud(font_path='fonts/TaipeiSansTCBeta-Regular.ttf').generate(seg_words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

