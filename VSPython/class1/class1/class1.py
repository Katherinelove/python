class Person:
    age=3
    height=170
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

tom=Person("tom")
jerry=Person("jerry",20)

print("="*30)
tom.show()
jerry.show()

print("="*30)
print(Person.__class__)
print(tom.__class__)

print("="*30)
print(Person.__name__)
print(tom.__class__.__name__)
print(jerry.__class__.__name__)

print("="*30)
print(Person.__qualname__)
print(tom.__class__.__qualname__)

print("="*30)
print(Person.__dict__)
print(tom.__dict__)
print(jerry.__dict__)


print("="*30)
Person.__dict__["show"](tom)
Person.__dict__["show"](jerry)

print("="*30)
Person.age=30
print(Person.age,tom.age,jerry.age)

print("="*30)
print(Person.height,tom.height,jerry.height)
print(Person.__dict__,tom.__dict__,jerry.__dict__)
print("="*30)
tom.height=182
print(Person.height,tom.height,jerry.height)
print(Person.__dict__,tom.__dict__,jerry.__dict__)
print("="*30)
jerry.height+=20
print(Person.height,tom.height,jerry.height)
print(Person.__dict__,tom.__dict__,jerry.__dict__)