import os
f=open("1.text","a")
f.write("hongliu\n lianghui\n wuyue\n")
f.close()
g=open("1.text","r")
loves=[line.strip("\n") for line in g.readlines()]
for i,love in enumerate(loves):
    print("第{}行为：{}".format(i+1,love))

print(os.listdir("."))
print(os.stat("1.text").st_size)