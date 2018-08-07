#coding:utf-8
#url下载
#author:katherinelove
#copyright:shuai

import requests

class HtmlDownload():
    """
    Html下载器
    """
    def download(self,url):
        if url is None:
            return None
        user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers={'User-agent':user_agent}
        response=requests.get(url,headers=headers)
        #响应成功修改encoding
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None

