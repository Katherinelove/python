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
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的url集合
        :param page_url:下载页面的url
        :param soup: soup
        :return: 返回新的url集合
        '''
        new_urls=set()
        #抽取符合要求的的a标记
        links=soup.find_all('a',href=re.compile(r'/item/.\d+'))
        for link in  links:
            #提取href属性
            new_url=link.get('href')
            #拼接成完整网址
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的url
        :param soup: soup
        :return: 返回有效数据{}
        '''
        data={}
        data['url']=page_url
        title=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        #soup查找对象.string   ==    soup查找对象.get_text()
        data['title']=title.get_text()
        summary=soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()
        return data