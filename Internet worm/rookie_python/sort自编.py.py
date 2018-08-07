import random


def get_a_list(num):
    lst=[]
    for i in range(num):
        lst.append(random.randint(1, 100))
    return lst

def sort_self(lst,asc=True):
    newlist=[]
    flag=False
    for x in lst:
        for i,y in enumerate(newlist):
            flag=x<y if asc else x>y
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

a=get_a_list(10)
print("排序之前:",a)

b=sort_self(a)
print("排序之后：",b)