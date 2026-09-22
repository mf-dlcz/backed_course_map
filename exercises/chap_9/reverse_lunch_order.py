"""

REVERSE LUNCH ORDER:

Complete the reverse_launch_order function.

It should take a list of rocket names and return a new list containing the same names in reverse order.

Use a loop and list indexing. Do not use list slicing or the .reverse() method. The original list should remain unchanged.

For example:

rockets = ["Scout", "Voyager", "Atlas"]
print(reverse_launch_order(rockets))
# ["Atlas", "Voyager", "Scout"]

print(rockets)
# ["Scout", "Voyager", "Atlas"]

"""

def reverse_launch_order(rockets):
    new_list = []

    for rocket in range(len(rockets)-1, -1, -1):
        new_list.append(rockets[rocket])
    return new_list
