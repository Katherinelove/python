import json

filename="username.json"
try:
    with open(filename) as file_object:
        username=json.load(file_object)
except:
    username=input("what' your name?")
    with open(filename,"w") as file_object:
        json.dump(username,file_object)
        print("I will remeber you when you come back!")
else:
    print("welcome back!"+username)