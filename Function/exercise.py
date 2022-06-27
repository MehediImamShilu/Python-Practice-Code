# Fizz Buzz Algorithm

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:  # No need for elif clause
        return "Fizz"
    if input % 5 == 0:  # No need for elif clause
        return "Buzz"
    return input


print(fizz_buzz(5))
