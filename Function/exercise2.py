# Define 2 functions with return value
# Call those two funcions with another new function

def start_sentense():
    return "More organized code", "More readable code", "Easier code reuse"


def second_sentense(hello):
    return "%s is a benefit of functions!" % hello


def final_sentense():
    copy_sentense = start_sentense()
    for hello in copy_sentense:
        print(second_sentense(hello))


final_sentense()
