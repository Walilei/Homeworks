def ptt_to_txt(article):

    content = article.find('div', {'id': 'main-content'}).text.split('--\n※ 發信站')[0]
    info = []
    for i in article.find_all('span', {'class': 'article-meta-value'}):
        info.append(i.text)
    author = info[0]
    # 修改標題去除特定字元，之後用作檔名
    title = info[2].replace(':', '_').replace('/', '-')
    time = info[3]

    like = 0
    dislike = 0
    for i in article.find_all('div', {'class': 'push'}):
        if i.text[0] == '推':
            like += 1
        elif i.text[0] == '噓':
            dislike += 1
    score = like - dislike

    # 存成文字檔
    with open(f'./ptt_movie/{title}.txt', 'w', encoding='utf-8') as file:
        file.write(content + '\n')
        file.write('--我是分隔線--' + '\n')
        file.write(f"推： {like}" + '\n')
        file.write(f"噓： {dislike}" + '\n')
        file.write(f"分數： {score}" + '\n')
        file.write(f"作者： {author}" + '\n')
        file.write(f"標題： {title}" + '\n')
        file.write(f"時間： {time}" + '\n')
