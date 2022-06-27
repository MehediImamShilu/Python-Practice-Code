smallest = None
print("Start", smallest)

for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)

print("End", smallest)
