"""
BUILD TRAVEL PACKING LISTS

This challenge is only about creating lists with literals (the first lesson of chapter 9).

    - Do not use for loops
    - Do not use .append() or any other list methods
    - Just create lists directly with square brackets [] and values inside them

1. get_clothing_list()
Return a list of clothing items in this exact order:

["shirt", "pants", "socks", "jacket"]

2. get_tech_list()
Return a list of tech items in this exact order:

["phone", "charger", "laptop", "headphones"]

3. get_full_packing_list()
This should return a single list that combines your other lists and a few extra items.

- The list must contain three elements in this order:

- The clothing list returned by get_clothing_list()

- The tech list returned by get_tech_list()

- A list of important documents: ["passport", "tickets", "wallet"]

So when everything is correct, this call:

print(get_full_packing_list())

should produce a list like:

[
    ["shirt", "pants", "socks", "jacket"],
    ["phone", "charger", "laptop", "headphones"],
    ["passport", "tickets", "wallet"],
]

You must use the get_clothing_list() and get_tech_list() functions inside get_full_packing_list() instead of typing their items again.

"""

def get_clothing_list():
    clothing_items = ["shirt", "pants", "socks", "jacket"]
    return clothing_items

def get_tech_list():
    tech_items = ["phone", "charger", "laptop", "headphones"]
    return tech_items

def get_full_packing_list():
    packing_list = ["passport", "tickets", "wallet"]
    clothing = get_clothing_list()
    tech = get_tech_list()
    return [clothing, tech, packing_list]