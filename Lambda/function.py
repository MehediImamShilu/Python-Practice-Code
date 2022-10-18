# anonymous function i s inside a regular function

def my_func(x):
    return lambda a: a * x


my_multiply = my_func(5)
my_triple = my_func(7)

print(my_multiply(10))
print(my_triple(12))
