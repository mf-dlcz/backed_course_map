"""
BUILDING A PACKING LIST

Complete the build_packing_checklist function.

It takes:

- items: a list of items to pack

- repeat_count: how many times each item should appear

Build and return a new list. Process the items in order, appending each item the specified number of times before moving to the next item.

Return an empty list when items is empty or repeat_count is zero or negative.

For example:

build_packing_checklist(["shirt", "socks"], 2)
# ["shirt", "shirt", "socks", "socks"]

Use .append() to add each entry to the new list.


"""

def build_packing_checklist(items, repeat_count):
    new_list = []

    for item in items:
        for repetition in range(repeat_count):
            new_list.append(item)
    return new_list