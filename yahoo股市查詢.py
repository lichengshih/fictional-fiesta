import requests
import time
from bs4 import BeautifulSoup
stock_code=str(input('請輸入股票代號:'))
url='https://tw.stock.yahoo.com/quote/'+stock_code+'.TW'
# print(url)
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
webpage=requests.get(url, headers=HEADERS)
soup=BeautifulSoup(webpage.text, 'html.parser')
tsmc=soup.find_all('div', {'id':"main-0-QuoteHeader-Proxy"})
# print(tsmc)
while True:
    for i in tsmc:
        stock_id=i.find('h1',{'class':'C($c-link-text) Fw(b) Fz(24px) Mend(8px)'}).text
        stock_price=i.find('span', {'class':"Fz(32px)"}).text
    print(stock_id,stock_price)
    time.sleep(30)