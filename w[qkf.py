import requests

a=requests.get('http://api.vworld.kr/req/address?service=address&request=getcoord&version=2.0&crs=epsg:4326&address=안양시 동안구 부림로169번길 22&refine=true&simple=false&format=json&type=road&key=B46A1ECD-5D5C-34C1-B38B-AAA4ACD090AE')
print(a.json())
