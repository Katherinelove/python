
def setproperty(name):
    def wrap(cls):
        cls.name=name
        return cls
    return wrap

@setproperty("zengshuai")
class Person:
    """初为人妻 余生请多多指教！"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    @classmethod
    def classmtd(cls):
        print(cls.name)
        print("{0.__name__}({0})".format(cls))

    @staticmethod
    def staticmtd():
        print("love you!")

tom=Person("tom",20)
Person.classmtd()
Person.staticmtd()
print(Person.__doc__)