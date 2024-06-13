import requests
from bs4 import BeautifulSoup
url='https://m.momoshop.com.tw/search.momo?_advFirst=N&_advCp=N&curPage=1&searchType=1&cateLevel=2&ent=k&searchKeyword=%E9%9B%BB%E8%85%A6&_advThreeHours=N&_isFuzzy=0&_imgSH=fourCardTypehttps://blog.csdn.net/lch551218/article/details/106026865'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
webpage= requests.get(url,headers=HEADERS)
# print(webpage.text)
soup=BeautifulSoup(webpage.text, 'html.parser')
momo=soup.find_all('li', {'class':'goodsItemLi goodsItemLiSeo'})
# print(momo)
for i in momo:
    item=i.find('h3', {'class':'prdName'}).text
    price=i.find('b', {'class':'price'}).text
    print('商品:',item ,'價格:',price)
