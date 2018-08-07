#!/usr/bin/python
import json

data = { 'g' : 1, 'b' : 2, 'c' : 3, 'h' : 4, 'e' : 5 }
data_1=("zengshui","hongliu","wuyue")
data_2="adfasfasfsafsaf"
json1 = json.dumps(data,sort_keys=True,indent=5)
json2=json.dumps(data_1,indent=5,sort_keys=True)
json3=json.dumps(data_2,indent=5,sort_keys=True)
print(type(json1))
print(json1)
print(json2)
print(json3)