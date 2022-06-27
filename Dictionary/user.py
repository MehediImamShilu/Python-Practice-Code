# From: Python Crush Course
# Dictionary is in a dictionary

# Multi users dictionary
users = {
    "shilu": {
        "first_name": "mehedi",
        "last_name": "imam",
        "location": "bangladesh"
    },

    "dolon": {
        "first_name": "ferdous",
        "last_name": "imam",
        "location": "germany"
    }
}

# loop for indivisual output
for user_name, user_info in users.items():
    # print users name
    print("\nUsername: " + user_name)
    full_name = user_info["first_name"] + " " + user_info["last_name"]
    location = user_info["location"]

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
