"""

Slicing a List:

Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

- First, return a slice of the champions list that starts with the third champion and goes to the end of the list.

- Next, return a slice of the champions list that starts at the beginning of the list and includes all champions 
except for the very last champion.

- Last, return a slice of the champions list that only includes the champions in even numbered indexes (0, 2, 4, ...).

* Tips
Remember, you can return multiple values from a function by separating them with commas:

- return value1, value2, value3

Zero is an even number

"""

def get_champion_slices(champions):
    list_one = champions[2:]
    list_two = champions[:-1]
    list_three = champions[::2]

    return list_one, list_two, list_three