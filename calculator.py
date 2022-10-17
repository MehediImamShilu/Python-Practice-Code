# Sample calculator in Python

def add(p, q):
    return p + q


def subtract(p, q):
    return p - q


def multiply(p, q):
    return p * q


def division(p, q):
    return p/q


print("Please select any one option: ")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice = input("Please enter choice (a/b/c/d): ")

number_one = int(input("Please enter first number: "))
number_two = int(input("Please enter second number: "))

if choice == "a":
    result = add(number_one, number_two)
    print(number_one, "+", number_two, "=", result)
elif choice == "b":
    result = subtract(number_one, number_two)
    print(number_one, "-", number_two, "=", result)
elif choice == "c":
    result = multiply(number_one, number_two)
    print(number_one, "*", number_two, "=", result)
elif choice == "d":
    result = division(number_one, number_two)
    print(number_one, "/", number_two, "=", result)
