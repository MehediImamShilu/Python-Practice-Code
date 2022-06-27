# NOTE: This is not actual code with print function
# Comprehension is used in case of map() & filter() function
# Comprehension is much more cleaner than map & filter
# Example is given below

items = [
    ("Product1", 7),
    ("Product2", 11),
    ("Product3", 45)
]

# Here, Line 13 & 14 are basically same for mapping
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]    # cleaner code

# Here, Line 17 & 18 are baically same for filtering
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]    # cleaner code
