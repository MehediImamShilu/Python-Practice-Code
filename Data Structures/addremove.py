letters = ["a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "-")

# remove
letters.pop(0)  # positional index
letters.remove("c")     # value from the list
del letters[0:2]    # range
letters.clear()     # empty function
print(letters)
