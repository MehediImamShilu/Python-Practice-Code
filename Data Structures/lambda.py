# code is same as sort2.py file in this directory
# without using function, lambda can be used

items = [
    ("Product01", 44),
    ("Product02", 65),
    ("Product03", 29)
]

# Here key=lambda is default keyword
# after key=lambda, parameter:expression
# Here parameter is the name & expression is number list
items.sort(key=lambda item: item[1])
print(items)
