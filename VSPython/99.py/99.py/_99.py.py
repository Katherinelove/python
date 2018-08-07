print("打印99乘法表：");
for i in range(1,10):
    for j in range(1,i+1):
        # print("{0}*{1}={2:<2}".format(j,i,j*i),end=" ");
        print(str(j)+"*"+str(i)+"="+str(j*i)+"\t",end=" ");
    print();

     