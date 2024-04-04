# messing with JSON
# this program is to demonstrate storing 
# data in a json format

import json
import json
electricbill = {
    'name' : 'Andrew',
    'amount':'99999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricbill, f) # writes the dictionary object to the file as a JSON object

