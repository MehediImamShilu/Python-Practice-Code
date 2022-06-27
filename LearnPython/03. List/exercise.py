# defining x & y as an object
x = object()
y = object()

# assign list for 10 times with x & y
x_list = [x] * 10
y_list = [y] * 10
big_list = (x_list + y_list)

# print out the number of items in the list & len
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# checking the number of items by running if clause
if x_list.count(x) == 10 & y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 & big_list.count(y) == 10:
    print("Great!!!")
