count = 0
sum = 0
print("Start", count, sum)

for the_num in [9, 41, 12, 3, 74, 15]:
    # counting the total value from the list
    count = count + 1
    # summing the value of list
    sum = sum + the_num
    print(count, sum, the_num)

average_num = sum / count
print("End:", count, sum, average_num)
