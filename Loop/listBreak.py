# after printing "Mango", code will be break

fruits = ["Apple", "Mango", "Jackfruit"]
for x in fruits:
    print(x)
    if x == "Mango":
        break
