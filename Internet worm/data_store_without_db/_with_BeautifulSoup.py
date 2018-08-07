#以盗墓笔记（http://seputu.com/）为例，抽取出盗墓笔记的标题、章节、章节名称、和连接
#声明 这是一个静态网站，爬取的东西不是由JavaScript动态加载的  这是大前提

import requests
from bs4 import BeautifulSoup
import json

#requests请求响应
user_agent='Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
headers={user_agent:user_agent}
url='http://seputu.com'
response=requests.get(url)
print(response.status_code)
#print(response.text)

#解析网页，解析的string为response.text
#soup=BeautifulSoup(response.text,'html.parser') #当用lxml解析出现空白时，用html.parser解析
soup=BeautifulSoup(response.text,'lxml')   #lxml
print("盗墓笔记共{}篇：".format(len(soup.find_all(class_='mulu'))))   #返回满足搜索条件的列表
content=[]
for mulu in soup.find_all(class_='mulu'):
    h2=mulu.find('h2')     #返回第一个
    #获取标题
    if h2!=None:
        h2_title=h2.string
        #print(h2_title)
        lst=[]
        # 获取所有的a标记中url和章节内容
        for a in mulu.find(class_='box').find_all('a'):
            # mulu.find(class_='box')寻找当前节点mulu中的第一个类名为：box的节点，在此节点再查询所有的a标记（严谨性）
            href = a.get('href')  # 标记.get(属性名)   获取属性值
            box_title = a.get('title')
            #print(href, box_title)
            lst.append({"href":href,"box_title":box_title})
        content.append({"title":h2_title,"content":lst})


#存储为json格式
with open("盗墓笔记.json","w") as fp:
    json.dump(content,fp,indent=2)
with open("盗墓笔记.json","r") as fp:
    data=json.load(fp)
    print(data)
