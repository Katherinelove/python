def power(num):
    sum=num*num
    return sum
print(power(5))
def love(num,n=3):
    sum=1
    while n>0:
        n=n-1
        sum=sum*num
    return sum
print(love(5,2))
print(love(5))

def person(name,gender,age=6,city="beijing"):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)
person("zengshuai","m")
print("="*15)
person("guinv","f")