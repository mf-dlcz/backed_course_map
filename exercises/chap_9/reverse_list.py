"""

Reverse List:

Some of our players would like to view their inventories in reverse order.

Using a loop, let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

"""

def reverse_list(items):
    new_list = []

    for item in range(len(items) -1, -1, -1):
        new_list.append(items[item])
    return new_list