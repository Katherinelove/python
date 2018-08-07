names=["zeng shuai","hong liu" ,"liang hui  ","wu yue"]
for name in names:
    print("mr "+name.strip().title()+",please join my party!")
print("#"*20)

#聚会
print("{} 无法参加今晚聚会".format(names[2]))
names[2]="wu yan zu"
print("今晚聚会新名单")
for name in names:
    print("mr "+name.strip().title()+",please join my party!")
print("#"*20)
print("今晚找到一个大餐桌，我们多邀请几位一起嗨个痛快！！！")
names.insert(0,"liu shishi")
names.insert(len(names)//2,"yang mi")
names.append("an yixuan")
for name in names:
    print("mr "+name.strip().title()+",please join my party!")
print("#"*20)
print("sorry,今晚只能有个人聚会了，改日再来！！！")
print(len(names))
del names[len(names)-1]
print(len(names))
for i in range(len(names)-2):
    x=names.pop()
    print("sorry! {}今晚临时有事，改日再约！".format(x))
print(names)
print(bool(len(names)==2))