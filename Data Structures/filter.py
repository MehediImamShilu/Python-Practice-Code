# filter a list using filter, lambda & list funtions

items = [
    ("Product1",  20),
    ("Product2", 10),
    ("Product3", 9)
]

# filter function has function & iterable value
# It's included with lambda, boolean comparison & value of tuple list
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
