lvyou=["jiu zai gou","da LI","SAn ya","Gui lIn","daO diNG"]
lst=[]
for i in lvyou:
    lst.append(i.strip().lower())
print(lst)
lst1=sorted(lst)
print(lst1)
print(lst)
print("*"*30)
lst1=sorted(lst,key=str,reverse=True)
print(lst1)
print(lst)
print("*"*30)
lst.reverse()
print(lst)
print(lst)
