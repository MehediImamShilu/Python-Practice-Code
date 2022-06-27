# From: Python Crush Course
# store a set of dictionaries in a list or
# a list of items as a value in a dictionary

# Make an empty list
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Print the number of total aliens
print("The total alien numbers are: " + str(len(aliens)))
