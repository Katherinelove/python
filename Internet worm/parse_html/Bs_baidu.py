import re
import requests
from bs4 import BeautifulSoup

html = r'https://www.baidu.com'
respond=requests.get(html)
respond.encoding="utf-8"
soup = BeautifulSoup(respond.text, "lxml")
#输出
print(soup.prettify())
#tag标记有name，attrs属性
print(soup.title)
print(soup.title.name)
#提取属性，为字典存储，用.get（）方法访问
print(soup.body.attrs)
#不用soup.body["link"],如果没有这个关键字会抛出异常
print(soup.body.get("link"))
print("="*50)
#提取字符串,string提取标记中最多一个子标记中的字符串，否则返回None，提取一个标记中的多个标记中的字符串用.strings
print(soup.title.string)
for string in soup.strings:
    print(string)
#.stripped_strings可以去掉输出字符串中包含的空格和空行
for string in soup.stripped_strings:
    print(string)

print("="*50)
#遍历文档
#直接子节点列表
print("直接子节点列表-->")
print(soup.head.contents)
#直接子节点生成器
print("直接子节点生成器-->")
for child in soup.head.children:
    print(child)

#子孙子节点访问descendants
print("子孙子节点访问descendants-->")
for child in soup.head.descendants:
    print(child)

#直接父节点.parent
print("直接父节点-->")
print(soup.title.parent)
#所有父节点.parents
for parent in soup.a.parents:
    print("tag:第一个<a>的所有父节点")
    print(parent.name)
#兄弟节点.previous_sibling  .next_sibling
#对当前节点的所有兄弟节点.previous_siblings  .next_siblings
#前后节点.previous_element    .next_element
#前后所有节点 .previous_elements    .next_elements

print("="*50)
#搜索文档树
print("搜索文档树")
#find_all(name,atrrs,recursive,text,**kwargs)
#name标记可以是字符串，正则表达式，列表，Ture和方法,返回列表,字符串对象自动忽略
print(soup.find_all('a'))
#以b开头的标记
print(soup.find_all(re.compile(r'^b')))
print(soup.find_all(['a','p']))\
#自定义方法
def has_class_id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print(soup.find_all(has_class_id))

#kwars参数--tag属性搜索
print(soup.find_all(id=True))
print(soup.find_all(href=re.compile(r'\w+www.\w+')))
#class是python关键字，如何利用class筛选？class_
print(soup.find_all('a',class_="mnav"))

#text  字符串搜索
print(soup.find_all(text="百度一下，你就知道"))
print(soup.find_all(text=re.compile(r'\W\S')))

#limit返回限制个数

#recursive递归循环，find_all()默认检索所有子节点，如果只想搜索tag的直接子节点，可以使用recursive=False