import requests
from bs4 import BeautifulSoup
# import panda as pd
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
url='https://www.ibon.com.tw/retail_inquiry_ajax.aspx'
payload={'strTargetField':'COUNTY','strKeyWords':'台北市'}
webpage=requests.post(url,data=payload,headers=HEADERS)
soup=BeautifulSoup(webpage.text, "html.parser")

tpe1=soup.find_all('tr',style='background-color:#FFFFFF;')
tpe2=soup.find_all('tr',style='background-color:#E9E9E9;')
tpe1.extend(tpe2)
for shop in tpe1:
    print(shop.text)