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
