# Converting all data types

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# convert into JSON:
# indent=4, It will be easier to read
# separators parameter to change default separator
# sort_keys=True; order the keys in the result
y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)

# the result is a JSON string:
print(y)
