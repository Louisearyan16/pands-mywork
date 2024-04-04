
'''''
car = {

   "make": "ford",
    "model": "mondeo",
    "year" : 2006,
    "owner": {
        "name":"andrew",
        "driver-number":1123
}
}
print(car["year"])
print(car["owner"].get("names"))



# car has 4 key value pairs
 #attr ="model"    
#print(car["make"])
#print(car[attr])
'''

car = {
    "make":'fiat',
    'model':'punto',
    'price':10000,
    'tags':['pre-owned', 'best buy', 'dealer']
}

#print(car)
for key, value in car.items():
    print(key, 'has value', value)
