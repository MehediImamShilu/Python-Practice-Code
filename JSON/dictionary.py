# JSON dictionary

import json

# some JSON
x = '{"name": "Shilu", "age": 25, "address": "Dhaka"}'

# JSON conversion
y = json.loads(x)

# This result is a python dictionary
print(y["age"])
