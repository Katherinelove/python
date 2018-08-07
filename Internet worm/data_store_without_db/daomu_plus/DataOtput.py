#coding:utf-8
#小数据输出为html格式
#author:katherinelove
#copyright:shuai

'''
两种方法：一是store_data(data)存储到内                                                                                                                            存中
二是：output_html输出为指定的文件格式
但是这只能针对小数据，大数据采用数据库分批存储
'''

import codecs

class DataOutput():
    def __init__(self):
        self.datas=[]

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=codecs.open("盗墓笔记.html",'w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        for list in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>" % data['summary'])
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()