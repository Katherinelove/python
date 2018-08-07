aliens={}
aliens["color"]="green"
aliens["point"]=5
print(aliens)
aliens["color"]="yellow"
print(aliens)
del aliens["color"]
print(aliens)
num=aliens.pop("point")
print(num)
print(aliens)
lst=list(range(10))
print(lst)
l=lst.pop(0)
print(l)
print(lst)