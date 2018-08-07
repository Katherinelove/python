import re

print("="*50)
#编译正则表达用r''
pattern=re.compile(r'\d+',re.I|re.M)
#match()方法是从开始匹配，即判断最前面是不是符合表达式
result1=re.match(pattern,'520')
#结果是匹配对象，需要用group（）方法取出
print(result1.group())

print("="*50)
result2=re.search(pattern,"lo520ah123")
print(result2.group())


print("="*50)
#将字符串按照正则表达式分割
result3=re.split(pattern,"love520,shuai23ja6512")
print(result3)

print("="*50)
result4=re.findall(pattern,"A1B2C3D4")
print(result4)

print("="*50)
#以迭代器方式返回匹配对象
result4=re.finditer(pattern,"A1B2C3D4")
for match in result4:
    print("{:3s}".format(match.group()),end="")

