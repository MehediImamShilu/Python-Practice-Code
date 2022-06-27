# set is a collection of value which can't be changed

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)   # "|" means all unique items
print(first & second)   # "&" means common items
print(first - second)   # "-" means difference between sets
print(first ^ second)   # "^" means items either in first or second sets, not both

# finds through loop
if 1 in first:
    print("Yes!")
