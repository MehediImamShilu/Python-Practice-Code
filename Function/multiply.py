# You have to multiply multiple numbers of a tuple

def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


result = multiply(2, 3, 4, 5)
print(result)
