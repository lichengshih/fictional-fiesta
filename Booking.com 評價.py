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




