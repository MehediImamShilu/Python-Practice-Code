# loop a list

letters = ["a", "b", "c"]
# """
items = [0, "a"]
index, letter = items   # this term will avoid tuple
for index, letter in enumerate(letters):
    print(index, letter)
# """
"""
for letter in enumerate(letters):
    # enumerate is a by dafault operator
    # enumerate produce iteration in tuple
    print(letter)   # print(letter) will produce tuple output
"""
