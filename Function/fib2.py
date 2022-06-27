# Fibonacci series using list

def fib2(n):
    """Fibonacci series containing in a list."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


fib_output = fib2(100)  # calling the function
print(fib_output)   # print the result
