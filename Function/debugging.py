# debugging code
# Multiplication of multiple number

def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
        return total    # debug here


print("Start")
print(multiply(1, 2, 3))
