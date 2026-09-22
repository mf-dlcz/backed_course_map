"""
FIX THE RETURN ROUTE:

The build_return_route function should return a new list containing the stops in reverse order.

The current function copies the stops in their original order instead.

Use the loop and list indexes to fix it. Do not change the original list.

route = ["Cabin", "Bridge", "Lake"]
print(build_return_route(route))
# ["Lake", "Bridge", "Cabin"]

print(route)
# ["Cabin", "Bridge", "Lake"]

"""

def build_return_route(route):
    return_route = []
    for index in range(len(route) -1, -1, -1):
        return_route.append(route[index])
    return return_route