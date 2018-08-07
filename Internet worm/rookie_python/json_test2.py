import json


f=open("car.json")
car=json.load(f)
print(json.dumps(car,indent=5))