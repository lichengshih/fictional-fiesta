from bs4 import BeautifulSoup
import requests
url='https://www.books.com.tw/web/sys_saletopb/books'
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
webpage=requests.get(url, headers=HEADERS)
soup=BeautifulSoup(webpage.text, 'html.parser')    
section=soup.find('div', {'class':"mod_a clearfix"})
best_seller=section.find_all('li',{'class':'item'})
print(best_seller)
for i in best_seller:
    rank=i.find('strong',{'class':'no'}).text
    book_name=i.find('div',{'class':'type02_bd-a'}).a.text
    author=i.find('ul',{'class':'msg'}).a.text
    print('排行:',rank)
    print('書名:',book_name)
    print('作者:',author,'\n')