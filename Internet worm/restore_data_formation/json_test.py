import json

#encode编码过程--将python对象转为json对象
#dumps()--生成一个字符串，屏幕显示用哪
#         --参数Skipkeys(False 如果遇见非python基本类型会报TypeError错)
#          ensure_ascii=True,改为False正常显示非ascii字符
#          indent=非负 自动格式化json格式
#         encoding=‘utf-8’处理中文时
#         sort_key=False:默认无关键字排序
#dump()--将python对象转换成JSON对象，并将对象通过fp文件流写入文件中


#解码parse 将json对象转为python对象
#json.load(）--读取文件流中的json转为python对象
#           encoding='utf-8'  指定编码格式
#           parse_float  若指定，str按照float解码调用
#           parse_int    若指定，str按照int解码调用

#json.loads()--读取字符串，变为python对象
str=[{"username":"曾帅","age":24},(2,3),1]
json_str=json.dumps(str,ensure_ascii=False)   #显示用转为字符串
print(json_str)
with open("katherine.txt",'w') as fp:
    json.dump(str,fp,indent=2)
with open("katherine.txt") as fp:
    data=json.load(fp)
    print(data)

