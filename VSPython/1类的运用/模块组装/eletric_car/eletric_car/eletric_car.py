class Eletric_car(Car):
    def __init__(self,make,modle,year):
        super().__init__(make,modle,year)
        self.battery=Battery()

