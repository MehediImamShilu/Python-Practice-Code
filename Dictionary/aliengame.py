# From: Python Crush Course
# Change the colour of first 3 the alien

# Create an empty list
aliens = []

# Create 30 alien with green colour
for alien_number in range(0, 30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Change the first 3 colour
for alien in aliens[0:3]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

# Check if the colour is changed
for alien in aliens[0:5]:
    print(alien)
print("...")
