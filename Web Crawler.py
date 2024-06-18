import requests
from bs4 import BeautifulSoup
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
url='https://www.booking.com/reviewlist.zh-tw.html?aid=376396&label=booking-name2-yefrPbbyS%2AFIINHgyCnmNgS411022708271%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9040379%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt1O4nYvDr1lms&sid=45e726a69743a3f4b25b4a4afde9670c&srpvid=817837f9bed401e8&;cc1=tw&pagename=le-meridien-taipei&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_ye'
webpage=requests.get(url,headers=HEADERS)
soup=BeautifulSoup(webpage.text, 'html.parser')
section=soup.find('ul',{'role':'region'})
# print(section)
feedback_positive=section.find_all('div', {'class':'c-review'})
feedback_negative=section.find_all('div', class_='c-review__row')
# print(feedback_positive)
for i in feedback_positive:
    good=i.find('span', class_='c-review__body').text
    print(good)
for j in feedback_negative:
    worse=j.find('span', class_='c-review__body').text
    print(worse)

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

from bs4 import BeautifulSoup
import requests
for i in range(1,6):
    # print('網址:','https://www.cosme.net.tw/new-reviews?page='+str(i),'\n')
    url='https://www.urcosme.com/new-reviews?page='+str(i)
    HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    webpage=requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.text, "html.parser")
    # review=soup.find('div', {'class':'uc-reviews'})
    reviews=soup.find_all('div', {'class':'uc-review uc-review-with-product'})
    
    for i in reviews:
        comment=i.find('div', {'class':'two-line-dot uc-content-link'}).text
        author=i.find('div',{'class':'author-name'}).text
        status=i.find('div',{'class':'author-review-status'}).text
        rate=i.find('div', {'class':'review-score'}).text
        print('心得:',comment)
        print('作者:', author)
        print('狀態:',status)
        print('分數:',rate,'\n')

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


