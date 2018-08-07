from collections import namedtuple
import random
print(random.randint(2,10))
print(random.choice([2,1,0,5]))
print(random.randrange(2,10,2))
lst=range(4)
random.shuffle(lst)
print(lst)
point=namedtuple('p','x y')
p1=point(4,5)
print(p1)

student=namedtuple('s','name age')
s1=student('zengshuai',"20")
print(s1)
