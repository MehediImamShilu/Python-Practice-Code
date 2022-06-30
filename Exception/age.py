# Exception handling

try:
    # with statement
    """
    with open("age.py") as file:
        print("File Opened.")
    """
    age = int(input("Enter an age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid value.")
else:
    print("No exception were thrown.")
