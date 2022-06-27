# using of dictionaries

# point out dictionary with dict() function
point = dict(x=1, y=2)
point["z"] = 10
if "a" in point:
    print(point["a"])   # It's not found
print(point.get("a", 0))    # when "a" isn't found, it will print out none
# for point.get("a", 0), here 0 will produce 0, instead of none
del point["x"]      # for delete
print(point)

# iteration for printing out dict()
for key in point:
    print(key, point[key])
"""
# This is the same as upper iteration
for key, value in point.items():
    print(key, value)
"""
