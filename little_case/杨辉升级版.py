n=6
trag=[1,[1,1]]
for i in range(2,6):
    cur=[]
    oldline=trag[i-1].copy()
    oldline.append(0)
    oldline.insert(0,0)
    for j in range(len(oldline)-1):
        cur.append(oldline[j]+oldline[j+1])
    trag.append(cur)
#    oldline.clear()
print(trag)
