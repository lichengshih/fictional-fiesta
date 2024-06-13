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