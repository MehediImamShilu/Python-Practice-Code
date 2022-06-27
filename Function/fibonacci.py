# fibonacci series

def fibonacci(num):
    """Print a fibonacci series up to num"""
    a, b = 0, 1
    while a < num:
        print(a, end=" ")   # end=" " is the space between numbers
        a, b = b, a + b
    print()


fibonacci(2000)
