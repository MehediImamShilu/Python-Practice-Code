# use arbitrary number of keywords
# use asterisk

def build_profile(first, last, **user_info):
    """Build a dictionary which contains any kinds of value."""
    profile = {}
    # "first_name" will be stand before 'first' parameter
    profile["first_name"] = first
    # "last_name" will be stand before 'last' parameter
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("Mehedi", "Imam",
                             location="Jhenaidah",
                             field="Data Science")
print(user_profile)
