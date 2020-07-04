import requests
import json
import re
import csv

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/83.0.4103.116 Safari/537.36'
product_info = {}
spec_list = ["Contains", "Form", "State of Readiness", "Store", "Package Quantity", "Package type",
             "Net weight"]  # 要取得的specifications項目

with open('keywords.csv', newline='', encoding='utf-8') as csvfile:
    products = csv.reader(csvfile)
    for product in products:
        product_query = product[0] + ', ' + product[1]
        json_url = 'https://redsky.target.com/v2/plp/search/?' \
                   'channel=web&count=6&default_purchasability_filter=true' \
                   '&facet_recovery=false&fulfillment_test_mode=grocery_opu_team_member_test' \
                   f'&isDLP=false&keyword={product_query}&offset=0&pageId=%2Fs%2F{product_query}&pricing_store_id=3321' \
                   '&store_ids=3321%2C3277%2C3249%2C3312%2C3284&visitorId=01730534EA6202019A76E876D860158E' \
                   '&include_sponsored_search_v2=false&ppatok=AOxT33a&platform=desktop' \
                   f'&useragent={user_agent}' \
                   '&excludes=available_to_promise_qualitative%2Cavailable_to_promise_location_qualitative' \
                   '&key=eb2551e4accc14f38cc42d32fbc2b2ea'
        req = requests.get(json_url)
        json_string = json.loads(req.text)  # python的字典格式
        p_nums = len(json_string['search_response']['items']['Item'])

        for i in range(p_nums):
            product_info['query'] = product_query
            product = json_string['search_response']['items']['Item'][i]
            if 'title' in product.keys():                                        # 商品名稱
                product_info['name'] = product['title']
            if 'url' in product.keys():
                product_info['url'] = "https://www.target.com" + product['url']  # 商品網址
            if 'brand' in product.keys():
                product_info['brand'] = product['brand']  # 商品品牌
            if 'images' in product.keys():
                product_info['image_url'] = product["images"][0]["base_url"] + product["images"][0]["primary"]  # 商品圖片網址
            if 'price' in product.keys():
                try:
                    product_info['price'] = product["price"]["current_retail"]  # 商品價格
                except KeyError:
                    product_info['price'] = product["price"]["current_retail_min"]  # 最低價格
            if 'average_rating' in product.keys():
                product_info['average_rating'] = product["average_rating"]  # 評分分數
            if 'total_reviews' in product.keys():
                product_info['average_rating'] = (product["average_rating"], product["total_reviews"])  # 評分分數和人數
            if 'wellness_merchandise_attributes' in product.keys():
                product_info['At a glance'] = []
                for i in product['wellness_merchandise_attributes']:
                    product_info['At a glance'].append(i['value_name'])  # 商品特別標籤
            if 'soft_bullets' in product.keys():
                if 'bullets' in product['soft_bullets'].keys():
                    product_info['highlights'] = product['soft_bullets']['bullets']  # 商品特色
            if 'bullet_description' in product.keys():
                product_info['Specifications'] = {}
                for tag in spec_list:                             # 拿specifications跟spec_list比對後加入
                    for j in product["bullet_description"]:
                        j = j.replace("<B>", "").replace("</B>", "")
                        if re.match(tag, j):
                            product_info['Specifications'][tag] = j.split(": ")[1]    # 商品規格
            if 'top_reviews' in product.keys():
                product_info['top_reviews'] = []
                for _ in product['top_reviews']:
                    product_info['top_reviews'].append(_['review_text'])    # 最佳評論

            print(product_info)
