# ** (double asterisk) arguments
# output will be shown in "dictionary" format

def user_info(**user):
    print(user)     # user as a list: user["id"] or ["name"] or ["age"]
    print(user["name"])


user_info(id=1, name="Shilu", age=24)
