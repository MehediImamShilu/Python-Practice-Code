# Manually input the value
# With value, you have to welcome someone

def get_formatted_name(first_name, last_name):
    """Here is the full name."""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nFill up the value down below: ")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("First Name: ")  # if clause for quit the while loop
    if f_name == "q":
        break

    l_name = input("Last Name: ")   # if clause for quit the while loop
    if l_name == "q":
        break

    get_name = get_formatted_name(f_name, l_name)
    print("\nWelcome, " + get_name + "!")
