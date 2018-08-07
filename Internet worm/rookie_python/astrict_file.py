#f=open("inventory.txt","w")
#f.write("eggs\t28\napples\t30\npink\t35")
#f.close()

#文件打开与写入
f=open("inventory.txt","r")
lines=f.readlines()
items={}
for line in lines:
    line=line.strip("\n ")
    line=line.split("\t")
    items[line[0]]=line[1]
for k,v in items.items():
    print("{}：{}".format(k,v))
f.close()
