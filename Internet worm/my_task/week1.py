# codeing:utf-8

import requests
from bs4 import BeautifulSoup
import re



url='https://movie.douban.com/top250'
response=requests.get(url)
print(response.status_code)
print(response.encoding)
#print(response.text)
print('='*20+'html文本'+'='*20)
soup=BeautifulSoup(response.text,'lxml')
#print(soup.prettify())

content=[]
#解析文本
for id_content in soup.find_all(id='content'):
    h1= id_content.find('h1')      #注意string是附在tag对象的属性
    if h1:
        h1_title=h1.string
        print(h1_title)
        move_lst1=[]
        for item in id_content.find_all(class_='hd'):
            move_name=item.find(class_='title').string
            #print(move_name)
            move_href=item.find('a').get('href')
            #print(move_href)
            move_describle=item.find(class_='other').string
            #print(move_describle)
            move_lst1.append([move_name,move_href,move_describle])

        move_director_info = []
        for move_info in  id_content.find_all(class_='bd'):
            move_directors=move_info.find('p').strings
            #print(list(move_directors))
            for move_director in move_directors:
                #print(move_director)
                move_director_info.append(move_director.strip('/ . \n'))
        move_evaluation_lst=[]
        for evaluation in id_content.find_all(class_='star'):
            move_evaluation=evaluation.find(text=re.compile(r'评价'))
            #print(move_evaluation)
            move_evaluation_lst.append(move_evaluation)


        print(move_lst1)
        print(move_evaluation_lst)
        print(move_director_info)

