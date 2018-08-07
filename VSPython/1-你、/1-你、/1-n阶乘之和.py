
n=int(input("Please input a number:"))
sum=0;
mutiply=1;
for i in range(1,n+1):
    for j in range(1,i+1):
        mutiply*=j;
    sum+=mutiply;
    mutiply=1;
print(str(n));
print(str(n)+"的阶乘之和为：",sum);