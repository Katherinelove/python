class Car():
    def __init__(self,make,modle,year):
        self.make=make
        self.modle=modle
        self.year=year
        self.odometer_reading=0
    def change_make(self,make=""):
        if not make:
            message="input a new make:"
            make=input(message)
        self.make=make
    def change_modle(self,model=""):
        if not model:
            message="input a new modle:"
            model=input(message)
        self.modle=model
    def change_year(self,year=""):
        if not year:
            message="input a new year:"
            year=input(message)
        self.year=year
    def get_description(self):
        long_name=str(self.year)+" "+self.make+" "+self.modle
        return long_name


    def update_odometer(self,mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can not roll back an odometer")
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it!")


class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describle_battery(self):
        """打印电瓶容量消息"""
        print("this car has a "+str(self.battery_size)+"-kwh battery")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==80:
            range=270
        message="this car go approximately "+str(range)
        message+=" miles on a full charge"
        print(message)
        

class Eletric_car(Car):
    def __init__(self,make,modle,year):
        super().__init__(make,modle,year)
        self.battery=Battery()


my_car=Car("audi","A4",2015)
print(my_car.get_description())
my_car.change_make("pajiadi")
print(my_car.get_description())
my_car.change_year(2018)
print(my_car.get_description())

my_car.read_odometer()
my_car.update_odometer(20)
my_car.read_odometer()
my_car.update_odometer(15)
my_car.read_odometer()

my_tesla=Eletric_car("tesla","dazhong",2018)
my_tesla.battery.describle_battery()
my_tesla.battery.get_range()