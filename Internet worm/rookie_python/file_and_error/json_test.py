import  json

number=[2,3,4,5,6,7]

#将对象存储为json
filename="number.json"
with open(filename,"w") as file_object:
    json.dump(number,file_object)

#将json加载到python
filename="number.json"
with open(filename) as file_object:
    new_number=json.load(file_object)
    print(new_number)