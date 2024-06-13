import requests
from bs4 import BeautifulSoup
url='https://running.biji.co/index.php?q=news&label=5'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
webpage=requests.get(url, headers=HEADERS)
# print(webpage)
soup=BeautifulSoup(webpage.text, 'html.parser')
biji=soup.find_all('div', {'class':'postMeta-feedSummery'})
# print(biji)

for i in biji:
    title= i.find('h3',{'class':'news-title'}).text
    summery= i.find('p', {'class':'teaser'}).text
    print('標題:',title)
    print('摘要:', summery.strip())
    print('標題:',title,'\n','摘要:', summery.strip(),sep='')