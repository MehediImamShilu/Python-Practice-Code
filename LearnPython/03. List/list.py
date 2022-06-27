# create an empty list
myList = []

# append is used for joining the items of the list
myList.append(1)
myList.append(2)
myList.append(3)

# print: 1
print(myList[0])
# print: 2
print(myList[1])
# print: 3
print(myList[2])

# print out: 1, 2, 3
for x in myList:
    print(x)

print("\n")

# New Code
# you will need to add numbers and strings to the correct lists
# using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list
# words 'hello' and 'world' to the strings variable

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# append method
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

new_name = names[1]

# You have to print numbers, strings & new_name
print(numbers)
print(strings)
print("The second name of the list is: %s" % new_name)
