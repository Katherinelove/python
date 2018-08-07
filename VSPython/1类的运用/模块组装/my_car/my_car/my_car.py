from car import Car
from battery import Battery
from eletric_car import Eletric_car


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
