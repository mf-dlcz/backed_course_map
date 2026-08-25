"""

BUILDING RUNNING POINT TOTALS

Complete the build_running_totals function.

It receives a list containing the points earned each day. 

Loop through the list and return a new list containing the running total after every day.

Use .append() to add each running total to the new list. 

Do not change the input list or use advanced list operations.

If the input list is empty, return an empty list.

"""

def build_running_totals(daily_points):
    total_points = []
    total = 0
    
    for points in daily_points:
        total += points
        total_points.append(total)
    return total_points