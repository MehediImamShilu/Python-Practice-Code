# JSON dictionary

import json

# some dictionary
x = {
    "name": "Imam",
    "age": 25,
    "address": "Dhaka"
}

# dictionary conversion
y = json.dumps(x)

# This result is a JSON
print(y)
