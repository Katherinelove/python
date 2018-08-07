while True:
    print("输入一个数n：");
    n=int(input());
    list=range(1,n+1);
    sum=0;
    for i in list:
        if i%2:
            sum+=i;
    print(sum);
    