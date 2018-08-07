n=6
trag=[[1],[1,1]]
for i in range(2,n):
    pre=trag[i-1]
    cur=[1]
    for j in range(i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    trag.append(cur)
print(trag)
