# map function with lambda

items = [
    ("Product1", 30),
    ("Product2", 34),
    ("Product3", 23)
]

prices = list(map(lambda item: item[1], items))
for x in prices:
    print(x)
