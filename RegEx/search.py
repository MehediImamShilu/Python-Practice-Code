# Regular Expression
# built-in module: re

import re

# check if the string starts with "The" & ends with "Spain"
# if you ends "Spain.", it will be no match bcz of "."
text = "The rain in Spain"
x = re.search("^The.*Spain$", text)     # metacharacter

# check if there is the value
if x:
    print("Yes, there is a match!")
else:
    print("No match!")

# Search for the first white-space character in the string
y = re.search("\s", text)
print("The first white-space character is located in position:", y.start())
