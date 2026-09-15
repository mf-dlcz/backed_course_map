"""

First Element:

Let's keep improving our inventory system. Complete the get_first_item function. It takes a list as input.

- Return the first element from the items list.

- If items is empty, return the string "ERROR" instead.

💫 You can check if a list is empty by checking its length.

"""

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"

    else:
        return items[0]
