#coding:utf-8
#爬虫初始化模块,利用crawl方法传入入口Url
#author:katherinelove
#copyright:shuai

from five_models.DataOtput import DataOutput
from five_models.HtmlDownloader import HtmlDownload
from five_models.HtmlParse import HtmlParse
from five_models.UrlManager import UrlManager


class SpiderMan():
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownload()
        self.parser=HtmlParse()
        self.output=DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取看多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从url管理器获取新的url
                new_url=self.manager.get_new_url()
                #HTML下载器下载网页
                html=self.downloader.download(new_url)
                #HTML解析器抽取网页数据
                new_urls,data=self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接"%(self.manager.old_url_size()))
            except :
                print("Crawl failed")
                #数据存储器将文件输出成指定格式
            self.output.output_html()


if __name__=="__main__":
        spider_man=SpiderMan()
        spider_man.crawl("https://baike.baidu.com/item/网络爬虫/")
