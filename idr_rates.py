import requests

result = requests.get('http://www.floatrates.com/daily/idr.json')

for data in result.json().values():
    print(data['code'])
    print(data['alphaCode'])
    print(data['numericCode'])
    print(data['name'])
    print(data['rate'])
    print(data['date'])
    print(data['inverseRate'])
