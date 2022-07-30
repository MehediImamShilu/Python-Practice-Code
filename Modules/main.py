# NOTE: This code is incomplete

from sales import calc_shipping, calc_tax
import sales
import sys

# Shows the path location
print(sys.path)
print(dir(sales))
print(sales.__name__)
print(sales.__file__)
# print(sales.__package__)
# print(sales.__doc__)

# This code is for line 4
# import sales: imports all the functions from sales module
sales.calc_shipping()
sales.calc_tax()

# This code is for line 3
# from a module, imports especific functions
calc_shipping()
calc_tax()
