# Do not print "Mango"

fruits = ["apple", "Mango", "Jackfruit"]
for x in fruits:
    if x == "Mango":
        continue
    print(x)
