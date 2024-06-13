# import requests
# from bs4 import BeautifulSoup
# import random
# HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
# url = 'https://www.ptt.cc/bbs/Beauty/M.1691067605.A.23A.html'
# proxy_list = ['220.132.33.150:4145','123.205.68.113:8197','125.227.225.157:3389']
# ip = random.choice(proxy_list)
# webpage = requests.get(url, headers=HEADERS, proxies={'http':'http://'+ip}, cookies={'over18':'1'})
# soup=BeautifulSoup(webpage.text, 'html.parser')
# imgs = soup.find_all('img')
# name = 1
# for i in imgs:
#     print(i['src'])
#     jpg = requests.get(i['src'])
#     f = open(f'C:/Users/Admin/Pictures/untitled/{name}.jpg', 'wb')
#     f.write(jpg.content)
#     f.close()
#     name = name + 1
    

import requests
from bs4 import BeautifulSoup
import random
import re
import os
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
url = 'https://store.line.me/stickershop/product/17245847/zh-Hant'
proxy_list = ['220.132.33.150:4145','123.205.68.113:8197','125.227.225.157:3389']
ip = random.choice(proxy_list)
webpage = requests.get(url, headers=HEADERS)
soup=BeautifulSoup(webpage.text, 'html.parser')
# print(soup)
stickers = re.findall("(?:https)\S*(?:sticker.png)", str(soup))
sticker=(set(stickers))
name=1
filepath=r'C:\Users\Admin\Pictures\untitled-2'
if not os.path.exists(filepath):
    os.mkdir(filepath)
for i in sticker:
    png=requests.get(i)
    name=name+1
    with open (os.path.join(filepath,str(name)+'.png'),'wb') as file:
        file.write(png.content)
        



# from pytube import YouTube, Playlist
# import os
# p=Playlist('https://www.youtube.com/watch?v=ZPOfJ03k9Ug&list=PL9046FFC4EB5438ED&index=25')
# path=r'C:\Users\Admin\Downloads\YTVideo'
# if not os.path.exists(path):
#     os.mkdir(path)
# for video in p.videos:
#     video.streams.first().download(path)