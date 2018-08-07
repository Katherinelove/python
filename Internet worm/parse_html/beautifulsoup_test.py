from bs4 import BeautifulSoup
import re
from lxml import etree

#创建一个html字符串进行解析
html_str="""
<html><head><title>katherine love story</title><meta charset="utf-8"/></head>
<body>
<p class="title"><b>I love you for ever,qiaolan</b></p>
<p class="story">how long time no see!
<a href="http://www.baidu.com" class="sister" id="link1"><!--baidu--></a>
<a href="http://www.zhihu.com" class="sister" id="link2">zhihu</a>
<a href="http://www.taobao.com" class="sister" id="link3">taobao</a>
see you again!
</p>
</body>
</html>
"""

#解析字符串
#创建BeautifulSoup对象的两种方法
soup=BeautifulSoup(html_str,'lxml')   #一通过字符串创建
#soup=BeautifulSoup(open('index.html'))  #通过打开html文件创建



#打印文档内容
print(soup.prettify())

#BeautifulSoup对象的种类
#Tab  navigableString BeautifulSoup Comment
print("="*20+"BeautifulSoup对象的种类 Tab"+"+"*20)
#Tab   两个重要的属性  name  和 attribute
print(soup.title)
print(soup.a)  #此方法只能查询第一个
print(soup.p)

#每个Tag都有自己的.name
print(soup.name)
print(soup.title.name)

#attribute 操作方法与字典相同
print(soup.p['class'])
print(soup.p.get('class'))
#.attr取属性输出为字典
print(soup.p.attrs)

print("="*20+"BeautifulSoup对象的种类 NavigableString"+"="*20)
#获取标记内部文字.string
print(soup.p.string)
print(type(soup.p.string))


print("="*20+"BeautifulSoup对象的种类 BeautifulSoup"+"="*20)
#BeautifulSoup对象并=可当做特殊的Tag，虽然没有name和attribute属性，但可以获取
print(type(soup.name))
print(soup.name)
print(soup.attrs)

print("="*20+"BeautifulSoup对象的种类 Comment"+"="*20)
#前三几乎覆盖了html和xml所有的内容  但还有一些特殊对象，如文档注释部分
print(soup.a.string)
print(type(soup.a.string))



print("="*20+"遍历文档树"+"="*20)
#Tag对象中直接子节点的.contents（以列表形式列出子节点）和.children属性很重要
print(soup.head.contents)
print(len(soup.head.contents))
print(soup.head.contents[0].string)
print("@"*40)
#遍历节点contents中的子节点
for child in soup.head.contents:
    print(child)
#同理.children
for child in soup.head.children:
    print(child)
#遍历tag中都有子孙节点.descendant
for child in soup.head.descendants:
    print(child)
print("@" * 40)
#如何获取节点内容  三属性string strings stripped_strings
#.string使用于Tag中只包含1个或0个标记的内容提取,多余1个返回None
print(soup.head.string)
print(soup.title.string)
print(soup.html.string)
#.strings适用于Tag中包含多个字符串的情况，可以进行循环遍历
for string in soup.strings:
    print(string)
#.stripped_stings可以除掉输出字符串中包含的空格和空行
for string in soup.stripped_strings:
    print(string)

#父节点.parent
print(soup.title)
print(soup.title.parent)

#.parents属性递归获取一个节点的所有父节点
print(soup.a)
print("*"*40)
for parent in soup.a.parents:
    #print(parent)    #打印所有父节点
    print(parent.name)

#兄弟节点.next_sibling或prev_sibling，不存在则返回None ;.next_siblings 或.previous_siblings
print("*" * 40)
print(soup.p.next_sibling)     #为什么为空白，因为空白或者换行也被视为一个节点
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)
print("*" * 40)
for sibling in soup.a.next_siblings:
    #print(sibling)
    print(repr(sibling))  #repr() 函数将对象转化为供解释器读取的形式，展示用

#前后节点.next_element和.previous_element  针对所有节点
print(soup.head)
print(soup.head.next_element)
#遍历节点之前/后的所有节点 .next_elements和.previous_elements
print("*"*40)
for element in soup.a.next_elements:
    print(repr(element))


#核心重点内容
print('='*20+'搜索文档树'+'='*20)
#重点介绍find_all方法--返回list   name参数可以为列表，字符串，正则表达式，True（all tag）,也可是自定义函数
for tag in soup.find_all(True):
    print(tag.name)
print(soup.find_all(name='b'))
print(soup.find_all(name=['a','b']))
print("*"*40)
#kwargs参数  可通过id属性查询tag
print(soup.find_all(id='link2'))

#查询有id的tag
for id_tag in soup.find_all(id=True):
    print(id_tag.name)

#想利用属性class过滤，但class为python关键字 方案：class后面加一个下划线
print(soup.find_all('a',class_="sister"))

#多个参数
print(soup.find_all(href=re.compile(r'baidu'),id='link1'))

#text参数用于搜索字符串  可以为列表，字符串，正则表达式，True
print("*" * 40)
print(soup.find_all(text=['zhihu','taobao']))
print(soup.find_all(text=re.compile(r'love')))

#limit参数  当文档树很大时，那么搜索很慢，当不需要全部结果，应用limit限制返回结果
print("*" * 40)
print(soup.find_all('a',limit=2))   #文档中满足条件的有三个，这儿限制查询两个后停止



#recursive（递归、循环）参数  True即查询所有子孙节点；false即只查询直接子节点
print(soup.find_all('title'))
print(soup.find_all('title',recursive=False))

#find_all(name,kwargs,text,limit,recursive)  返回一个列表
#find(name,kwargs,text,limit,recursive)    返回搜索结果中的第一个值 下同

#find_parents()
#find_parent()

#find_next_siblings()
#find_next_sibling()

#find_previous_siblings()
#find_previous_sibling()

#find_all_next() #获取字符串
#find_next()

#find_all_previous() #获取字符串
#find_previous()



#soup.select（） 类名前加. id名前加#  返回list
print('='*20+'CSS选择器'+'='*20)
#通过标记名称查询
print(soup.select('title'))
#逐层查找title
print(soup.select('head title'))
#查找xx标记下的XX soup.select('p > #id(.class)')   #注意  > 前后有空格
print(soup.select('p > #link2'))
print(soup.select('#link1 + .sister'))   # +    前后必须有空格

#class名查找
print(soup.select('.sister'))
#通过tag的id查找
print(soup.select("#link1"))
print(soup.select("a#link2"))
#通过是否有属性查找
print(soup.select('a[href]'))
#通过属性查找 属性是标签下的一个字典
print(soup.select('a[href="http://www.baidu.com"]'))

print('='*20+'lxml的Xpath解析'+'='*20)
#优点lxml一个非常实用的功能是自动修正html代码，末尾未闭合自动闭合
html=etree.HTML(html_str)
#lxml可以直接读取html文件，利用parse方法进行解析
#html=etree.parse('xxx.html')
print(html)
result=etree.tostring(html)
print(result)

#利用Xpath语法抽取其中所有的URL
urls=html.xpath(".//*[@class='sister']/@href")
#解释  取当前节点的（满足属性class=“sister”）所有所有元素 选取当前节点href属性
print(urls)