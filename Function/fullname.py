# print out full name
# A name might have two or three parts

def formatted_name(first_name, last_name, middle_name=""):
    # middle name should be a default empty parameter
    # everyone may not have a middle name
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


my_name = formatted_name("ferdous", "dolon")
print(my_name)

my_name = formatted_name("mehedi", "imam", "shilu")
print(my_name)
