import keyword
import sys

print(keyword.kwlist)

#注释
"""注释
    注释
"""
name='''i
love
you
'''
print(name)

full_name="zeng"+\
           "wei"+\
           "shuai"
print(full_name)
str1="abcdefghijk"
print("*"*0)
print(str1[0:-1])
print(str1*2)


hr="="*10+"Python import mode"+"="*10
print(hr)
print("命令行参数：")
for i in sys.argv:
    print(i)
print(sys.argv[0])
print(sys.path)
