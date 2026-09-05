"""
BUILD DELIVERY ROUTE:


Complete the build_delivery_route function.

It receives:

- A starting location
- A list of delivery stops
- A final destination
- Create a new empty list and use .append() to add the locations in this order:

The starting location
Each delivery stop, in order
The final destination
Return the completed route. Do not change the provided delivery_stops list.

For example:

route = build_delivery_route(
    "Warehouse",
    ["Bakery", "Library"],
    "Post Office",
)
print(route)
# ["Warehouse", "Bakery", "Library", "Post Office"]

"""

def build_delivery_route(start, delivery_stops, destination):
    route = []

    route.append(start)
    for stops in delivery_stops:
            route.append(stops)
    
    route.append(destination)
    
    return route