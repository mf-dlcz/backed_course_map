'''
The functions should:

return the correct value instead of the wrong one
use the correct parameter in the calculation
build the exact expected string
fix one scope bug where a function reads the wrong variable name
Do not use:

- if statements
- loops
lists, dictionaries, or sets

Expected behavior
make_badge(name, title)
Return a string in this format:

"{title}: {name}"
'''

station_name = "Orion Gate"


def make_badge(name, title):
    return f"{title}: {name}"


def add_supply(total, delivered):
    return total + delivered


def spend_credits(balance, cost):
    return balance - cost


def station_alert(captain):
    return f"Captain {captain} report to {station_name}"