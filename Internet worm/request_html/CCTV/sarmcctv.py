import requests

#添加请求头
user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers={'user_agent':user_agent}
r=requests.get("http://tv.cctv.com/",headers=headers)
print("*"*50)
#检验是否请求成
print("请求码-->"+str(r.status_code))
#r.header是字典，可以用get（）方法访问,不会抛出异常
print(r.headers)
print(r.headers.get('Server'))
print("*"*50)
#乱码
#print("text-->"+r.text)
print(r.content)
print("encoding-->"+r.encoding)
#修改编码，不会乱码
r.encoding="utf-8"
print("encoding-->"+r.encoding)
#print("new text-->"+r.text)
print("*"*50)
print("*"*50)
#只提取前面几行字节数；注意content显示为bytes对象
r1=requests.get("http://tv.cctv.com/",stream=True)
print(r1.raw.read(10))