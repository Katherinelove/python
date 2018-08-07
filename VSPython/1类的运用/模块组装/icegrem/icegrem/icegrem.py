class IceCreamStand():
    def __init__(self, name,style,flavors):
        self.name=name
        self.style=style
        self.flavors=flavors
    def describe_icecream(self):
        print(self.name+"\t"+self.style)
    def open_icecreamstand(self):
        print("this icecreamstand is opening!")

spice_lst=["花椒","八角","桂皮"]
my_icecream=IceCreamStand("snow","清爽可口",spice_lst)
print(my_icecream.flavors)
my_icecream.open_icecreamstand()
my_icecream.describe_icecream()