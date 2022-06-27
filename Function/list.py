# print every single name from the list

def user_name(name_list):
    for name in name_list:
        massage = "Hi, " + name.title()
        print(massage)


names = ["mehedi", "imam", "shilu"]
user_name(names)
