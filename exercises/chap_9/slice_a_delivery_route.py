"""

Slice a Delivery Route:

Complete the slice_route function.

It receives a list of at least four delivery stops. Return a new list containing these three sections, in order:

1. The first two stops
2. Every stop between the first two and last two stops
3. The last two stops

Use list slicing to create each section. Do not change the original list.

For example:

route = ["Bakery", "Library", "Market", "Cafe", "School"]
print(slice_route(route))

# [["Bakery", "Library"], ["Market"], ["Cafe", "School"]]

"""

def slice_route(route):
    route_one = route[:2]
    route_two = route[2:-2]
    route_three = route[-2:]
    
    return [route_one, route_two, route_three]