# Find out even & odd number into a fixed range
# Count total even & odd number

even_count = 0
odd_count = 0

for num in range(2, 10):
    if num % 2 == 0:
        print("Found the even number: ", num)
        even_count += 1
        continue

    else:
        print("Found the odd number: ", num)
        odd_count += 1

print("Total even number: ", even_count)
print("Total odd number: ", odd_count)
