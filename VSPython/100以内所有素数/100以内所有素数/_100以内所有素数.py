while True:
    m=int(input("please input a m:[m>2]"))
    for j in range(2,m+1):
        for i in range(2,j):
            if j%i==0:
                break
        else:
            print(j)
   
