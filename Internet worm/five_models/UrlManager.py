#coding:utf-8
#url管理器
#author:katherinelove
#copyright:shuai


#建立一个url管理器（class）
#判断是否有待取的url，   has_new_url()
#添加新的url到未爬去集合中，  add_new_url(url),add_new_urls(urls)
#获取一个未爬去的url，get_new_url()
#获取未爬取url集合大小， new_url_size()
#获取已经爬取的url集合大小， old_url_size()


class UrlManager():
    def __init__(self):
        '''set()去重,集合增加元素用add（）方法'''
        self.newurls=set()   #未爬去url集合
        self.oldurls=set()   #已爬取url集合

    def has_new_url(self):
        '''
        判断是否有未爬取得url
        :return:bools值
        '''
        return self.new_url_size()!=0

    def get_new_url(self):
        '''
        获取一个未爬取的url
        :return:
        '''
        new_url=self.newurls.pop()    #未爬取url集合弹出集合最后一个url
        self.oldurls.add(new_url)      #已爬取url集合增加一个url
        return new_url

    def add_new_url(self,url):
        '''
        将新的url添加到未爬取的集合中
        :param url: 单个url
        :return:
        '''
        if url==None:  #逻辑：url为空返回None
            return
        if url not in self.newurls and url not in self.oldurls:
            #新增url既不能在未爬取得url集合中，也不能在已爬取的集合中
            self.newurls.add(url)

    def add_new_urls(self,urls):
        '''
        将新的urls添加到未爬取的集合中
        :param urls: urls集合
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        获取未爬取的url集合的大小
        :return:
        """
        return len(self.newurls)

    def old_url_size(self):
        """
        获取已经爬去的url集合的大小
        :return:
        """
        return len(self.oldurls)