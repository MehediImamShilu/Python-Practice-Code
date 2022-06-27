# using of asterisk in function

def make_pizza(size, *pizza_list):
    print("\nMaking a " + str(size) + " inch following pizza: ")
    for pizza in pizza_list:
        print("-" + pizza)


# make_pizza(12, "Peporoni")
# make_pizza(16, "Chilli", "Mashroom", "Beef")

# Here, Functions are commented
# Note: This is a module function,
# which is used in "make_pizzas.py" in the same directory
