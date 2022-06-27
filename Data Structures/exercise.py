# Problem: Find out the most repeated character
# Exercise of Mosh Hamedani
# import pprint for controlling the output where module is also pprint

from pprint import pprint

sentense = "This is a common interview question"

# Naive method
char_frequency = {}
for char in sentense:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)
# Note: pprint() instead of print()

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
# sorted() converts the dict into list of tuple
# Note: dict() can't be sorted
# key=lambda kv: kv[1] shows the less to most key value
# reverse=True will reverse the key value from most to less

print(char_frequency_sorted[0])
