import requests

import json

a=requests.get('http://api.vworld.kr/req/address?service=address&request=getcoord&version=2.0&crs=epsg:4326&address=안양시 동안구 부림로169번길 22&refine=true&simple=false&format=json&type=road&key=B46A1ECD-5D5C-34C1-B38B-AAA4ACD090AE')
print(a.json())



xPoint=float(a.json()["response"]["result"]["point"]["x"])
yPoint=float(a.json()["response"]["result"]["point"]["y"])
print(xPoint,yPoint)
f = open("우리병원.csv")

hospital = f.read()

hospital.split(',')[0]

print(hospital)
