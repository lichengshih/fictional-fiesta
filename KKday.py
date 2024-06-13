import requests
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
url='https://www.kkday.com/zh-tw/product/ajax_get_autocomplete_prod_data?keywords=%E6%96%B0%E7%AB%B9%E5%B8%82&limit=5'

webpage=requests.get(url,headers=HEADERS)
content=webpage.json()['data']
# print(content)
for i in content:
    name=i['name']
    price=i['price']
    print('品名:',name,'價格:',price)