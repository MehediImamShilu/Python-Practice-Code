car = {
    "Brand": "Toyota",
    "Model": "Cemri",
    "Year": 2021
}

x = car.values()

# before updated
print(x)

# after updated
car["Year"] = 2022
print(x)
