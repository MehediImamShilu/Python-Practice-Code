# dictionary comprehension

"""
values = []
for x in range(5):
    values.append(x * 2)
"""
# Same as commented multiple lines (4 to 6)
values = {x: x * 2 for x in range(5)}
print(values)

# NOTE: This doesn't works for tuple
