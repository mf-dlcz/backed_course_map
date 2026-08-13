"""
Should Serve Drinks

Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. 

Only return True if all of these conditions apply. 

If any of these conditions are False, return False:

The customer's age is 21 or older

The bartender is working

The time is between 5 and 10 o'clock (inclusive of both 5 and 10)
"""

def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:
        return False
    return True