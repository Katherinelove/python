#coding:utf-8
#爬虫初始化模块,利用crawl方法传入入口Url
#author:katherinelove
#copyright:shuai

from data_store_without_db.daomu_plus.DataOtput import DataOutput
from data_store_without_db.daomu_plus.HtmlDownloader import HtmlDownload
from data_store_without_db.daomu_plus.HtmlParse import HtmlParse
from five_models.UrlManager import UrlManager


class SpiderMan():
    def __init__(self):
        self.downloader=HtmlDownload()
        self.parser=HtmlParse()
        self.output=DataOutput()

    def crawl(self,root_url):
        #添加入口url
        html = self.downloader.download(root_url)
        print(html)
        # HTML解析器抽取网页数据
        data = self.parser.parser(root_url, html)
        # 将抽取的url添加到url管理器中
        # self.manager.add_new_urls(new_urls)
        # 数据存储器存储文件
        print(data)
        self.output.output_html()


if __name__=="__main__":
        spider_man=SpiderMan()
        spider_man.crawl("http://www.seputu.com/")
