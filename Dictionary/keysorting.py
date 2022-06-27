# You have to sort the key name of dictionary

favourite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"}

for name in sorted(favourite_language.keys()):
    print(name.title())
# key name wil be printed as alphanumeric wise

print("\nThe following repeated language have be mentioned:")
for language in favourite_language.values():
    print(language.title())
# Values name will be printed even they are repeated

print("\nUnrepeated language:")
for unrepeated_language in set(favourite_language.values()):
    print(unrepeated_language.title() + " is mentioned in the dict.")
# set() will prevent repeated values
