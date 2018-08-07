file_name="11.txt"
with open(file_name) as file_object:
#    content=file_object.read()               #解读文件得到是字符串
#    for line in file_object:
#        print(line.strip())


    lines=file_object.readlines()       #得到是列表lines  可以在with语块外访问
    for num,line in enumerate(lines):
        print(str(num)+"-"+line.strip())


#外部使用文件内容，这里新建一个pi——string变量存储所有数字且没有空格
pi_string=""
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(pi_string[:10]+".....")    #切片只取前十位（包括小数点）


#检查自己的生日是否在圆周率中
my_birthday=input("enter your birthday!(930710)")
if my_birthday in pi_string:
    print("yes")
else:
    print("no")

#replace 修改字符串
print(pi_string.replace("3.14","3.15"))
print(pi_string)