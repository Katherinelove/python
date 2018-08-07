#爬虫中出现异常或服务器遇到问题，可以通过Email给自己发送报告
#发送邮件的协议是SMTP（stamp） python内置支持STMP，可以发送纯文本文件、HTML邮件和带附件邮件
#python支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发邮件
#前提条件，申请163.com邮箱并开启STMP功能，采用的网易电子邮箱的服务器stmp.163.com

"""
#构造一个纯文本邮件
from  email.mime.text import MIMEText
'''
构造MIMEtext（）对象需要3个参数
正文
MIME的subtype，传入'plain'表示纯文本，最终的MIME就是"text/plain" ;'html'表示文本为异常网页；
设置编码格式 utf-8
'''
msg=MIMEText('python爬虫运行异常，异常信息为遇到HTTP 403','palin','utf-8')
"""

#接着设置邮件的发件人、收件人、和邮件主题等信息，并通过SMTP发送出去
from email.header import Header  #Header对象对字符（中文）进行编码
from  email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib



def _formation_addr(s):
    '''返回格式化字符串'''
    (name,addr)=parseaddr(s)      #解析字符串15281857366@163.com-->15281857366   @163.com
    return formataddr(Header(name,'utf-8').encode(),addr)   #再编码组装


#发件人地址
from_addr='15281857366@163.com'
#邮箱密码
password='zl.201314shuai'
#收件人地址
to_addr='1139774827@qq.com'
#163网易邮箱服务器地址
smtp_sever='smtp.163.com'

print(parseaddr("love <%s>"%from_addr))

#设置邮件信息
msg=MIMEText('python爬虫运行异常，异常信息为遇到HTTP 403','plain','utf-8')
msg['From']=_formation_addr("一号爬虫<%s>"%from_addr)        #发件人
msg['To']=_formation_addr('管理员<%s>'%to_addr)              #收件人
msg['Subject']=Header('一号爬虫运行状态','utf-8')   #后加.encode()  #主题

#发送邮件
sever=smtplib.SMTP(smtp_sever,25)
sever.login(from_addr,password)
sever.sendmail(from_addr,to_addr,msg.as_string())
sever.quit()