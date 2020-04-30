import requests
import json
from bs4 import BeautifulSoup

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

# 列印第1~6的頁面
for page in range(1, 6):
    post_data_str = f'''action: fm_ajax_load_more
    nonce: 025c2d58ba
    page: {page}'''
    post_data = {r.split(': ')[0]: r.split(': ')[1] for r in post_data_str.split('\n')}
    res = requests.post(url, headers=headers, data=post_data)
    json_data = json.loads(res.text)
    soup = BeautifulSoup(json_data['data'], 'html.parser')
    for tag in soup.select('h4'):
        title = tag.text
        website = tag.a['href']
        print(title)
        print(website)
        print('========')
