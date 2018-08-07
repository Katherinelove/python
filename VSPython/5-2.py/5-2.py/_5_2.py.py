while True:
    print("景区票价详情：")
    print("请输入你的年龄:",end="")
    age=input()
    if age=="quit":
       break
    if int(age)<=0:
        print("请输入正确的年龄！")
    if int(age)<10:
        price=10
    elif int(age)<20:
        price=20
    elif int(age)<30:
        price=30
    elif int(age)>=30:
        price=20
    print("{}岁票价是{}".format(age,price))


