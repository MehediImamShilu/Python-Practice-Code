# sorting a list of tuple

items = [
    ("Product01", 34),
    ("Product02", 54),
    ("Product03", 23)
]


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)
