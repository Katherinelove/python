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


