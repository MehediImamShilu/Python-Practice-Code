# You have to combine two list
# zip is used for combine two list

list1 = [1, 2, 3]
list2 = [10, 20, 30]
# print out should be: [(1, 10), (2, 20), (3, 30)]
# or, [(a, 1, 10), (b, 2, 20), (c, 3, 30)]

x = list(zip("abc", list1, list2))
print(x)
