# Two list
# Checking the similarities & find out similiar thing

first_toppings = ["mushrooms", "olives", "green peppers",
                  "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fry", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in first_toppings:
        print("Add " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished toppings.")
