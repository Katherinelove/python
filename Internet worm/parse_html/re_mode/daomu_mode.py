#利用json存储数据
#coding:utf-8
import requests
from bs4 import BeautifulSoup as bs
import json


html=r'http://seputu.com/'
respond=requests.get(html)
respond.encoding="utf=-8"
print(respond.status_code)

soup=bs(respond.text,'lxml')
#print(soup.prettify())
content=[]   #固定格式，总目录
for mulu in soup.find_all(class_='mulu'):
    h2=mulu.find('h2')
    if h2!=None:
        h2_title=h2.string
        #print(h2_title)
        lst=[]  #存储每章节
        for a in mulu.find(class_="box").find_all('a'):
            href=a.get("href")
            title=a.get("title")
            #print(href,title)
            lst.append({'title':title,'href':href})
        content.append({'Title':h2_title,'content':lst})

with open("daomu_plus.json","w") as fp:
    json.dump(content,fp,indent=4)

with open("daomu_plus.json","r") as fp:
    print(json.load(fp))