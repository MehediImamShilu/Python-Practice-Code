# List Loop
# finding the largest number

largest_num = -1
print("Start", largest_num)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_num:
        largest_num = the_num
    print(largest_num, the_num)
print("End", largest_num)
