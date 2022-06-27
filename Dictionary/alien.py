# Python Crush Course Book Practices

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x_position is: " + str(alien_0["x_position"]))

# run if-clause to find the speed & increse the speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be first alien
    x_increment = 3

alien_0["x_position"] = x_increment + alien_0["x_position"]
print("The new position is: " + str(alien_0["x_position"]))
