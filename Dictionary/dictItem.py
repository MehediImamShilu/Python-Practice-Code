thisDict = {
    "Brand": "Toyota",
    "Model": "Cemri",
    "Year": 2021
}
x = thisDict.items()

# before change
print(x)

# after change
thisDict["Year"] = 2022
print(x)

# adding items
thisDict["Colour"] = "Red"
print(x)
