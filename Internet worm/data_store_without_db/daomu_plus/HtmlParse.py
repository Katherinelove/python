#coding:utf-8
#Html解析
#author:katherinelove
#copyright:shuai

'''
利用Beautifulsoup解析HTML，这里提取词条的html和词条的url标题和摘要信息
'''
import re
#python3.0
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class HtmlParse():
    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取url和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载网页的内容
        :return:
        '''
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')
#        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(soup)
        return new_data

    def _get_new_data(self,soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的url
        :param soup: soup
        :return: 返回有效数据{}
        '''
        data=[]
        for mulu in soup.find_all(class_='mulu'):
            h2 = mulu.find('h2')  # 返回第一个
            # 获取标题
            if h2 != None:
                h2_title = h2.string
                # print(h2_title)
                # 获取所有的a标记中url和章节内容
                content=[]
                for a in mulu.find(class_='box').find_all('a'):
                    # mulu.find(class_='box')寻找当前节点mulu中的第一个类名为：box的节点，在此节点再查询所有的a标记（严谨性）
                    href = a.get('href')  # 标记.get(属性名)   获取属性值
                    box_title = a.get('title')
                    # print(href, box_title)
                    content.append({"href":href,"title":box_title})
                data.append({"character":h2_title,"content":content})
        return data






