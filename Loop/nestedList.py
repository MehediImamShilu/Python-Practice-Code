# first value of "color" will be collide with every value of "fruit"
# second & third value of color will also follow the same path

color = ["Purple", "Green", "Blue"]
fruit = ["apple", "banana", "orange"]

for x in color:
    for y in fruit:
        print(x, y)
