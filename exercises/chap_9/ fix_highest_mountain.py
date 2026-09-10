"""

FIX HIGHEST MOUNTAIN

The find_highest_elevation function should return the highest elevation in a list.

It works for elevations above sea level, but it gives the wrong answer when every elevation is negative. Fix the function so it works with both positive and negative values.

The input list will always contain at least one number.

find_highest_elevation([120, 450, 275])
# 450

find_highest_elevation([-80, -25, -140])
# -25


"""

def find_highest_elevation(elevations):
    highest = float("-inf")
    for elevation in elevations:
        if elevation > highest:
            highest = elevation
    return highest