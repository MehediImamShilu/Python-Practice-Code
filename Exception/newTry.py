# Python code illustration
# Working on try()

def divide(x, y):
    try:
        # Floor division
        result = x // y
        print("Yeah! Your answer is: ", result)
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero.")


divide(3, 2)
