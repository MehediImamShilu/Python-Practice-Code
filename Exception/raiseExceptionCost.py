# Exception through raise method
# This method is costly in time management
# Let's se how much costly during time management

# Calculate Time
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
# code1 shows more time costly

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
# code2 shows less time efficient

print("First code: ", timeit(code1, number=10000))
print("Second code: ", timeit(code2, number=10000))

# output: run through terminal
# Age can not be 0 or less
# First code: 2.4933267
# Second code: 0.00166329
# Moral: try not to use raise & use code2 format
