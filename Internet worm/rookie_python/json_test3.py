import json


class Car():
    def __init__(self,make,model,color,doors=4,feature={}):
        self.make=make
        self.model=model
        self.color=color
        self.doors=doors
        self.feature=feature

mycar=Car("ford","explorer","red",feature={"stowaway":True})

f=open("new_car.json","w")
json.dump(vars(mycar),f,indent=5)
f.close()

f=open("new_car.json")
new_car=json.load(f)
f.close()
print(new_car)
