# using "dictionary"

def build_person(first_name, last_name, age=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age     # for including age into dictionary
    return person


developer = build_person("mehedi", "imam", age=25)
print(developer)
