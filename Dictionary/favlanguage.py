# From: Python Crush Course
# Print out everyone's fav language in tab

favourite_languages = {
    "mehedi": ["python", "javascript"],
    "rasif": ["ruby"],
    "tanzil": ["c"],
    "esha": ["r", "go"],
    "sathi": ["typescript", "python"],
}

# use loop for names & languages in fav_lan
for names, languages in favourite_languages.items():
    print("\n" + names.title() + "'s favourite language is:")
    for language in languages:
        print("\t" + language.title())
