##多媒体文件抽取

import requests
from lxml import etree
#只能这么用urlretrieve函数（取回）
from urllib.request import urlretrieve

import os
#显示当前目录，改变当前目录
path = os.getcwd()
localpath = os.chdir(r'F:\pachong\my_task\week2_download')
print(localpath)



'''
 urllib.urlretrieve 的回调函数：
def callbackfunc(blocknum, blocksize, totalsize):
    @blocknum:  已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
'''

def Schedule(block_num,block_size,total_size):
    '''
    :param block_num:已经下载的数据块
    :param block_size: 数据块的大小
    :param total_size: 远程文件的大小
    '''
    per=100.0*block_num*block_size/total_size
    if per>100:
        per=100
        print("当前下载进度：%d"%per)


user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)'
headers = {"user_agent": user_agent}
response = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
# 使用lxml解析网页
html = etree.HTML(response.text)
img_urls = html.xpath('.//img/@src')  # 先找到所有的img
i = 0
for img_url in img_urls:
    # 注意urlretrieve（链接，自定义名称，自定义函数）
    urlretrieve(img_url, 'img' + str(i) + '.jpg', Schedule)
    i += 1

print("运行完毕！！！",i)

#本程序将img标记中的src属性提取出来，交个urlretrieve（）函数去下载，自动回调Schedule函数，显示当前下载的精度

