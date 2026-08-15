"""
SUM GAME

The sum_of_odd_numbers function should calculate the sum of all the odd numbers starting at 1 up 
to (but not including) the given end number and return the result.

Fix the loop so that it iterates over the correct numbers.

"""

def sum_of_odd_numbers(end):
    total = 0
    for i in range(0 + 1, end, 2):
        #print(i, "i")
        total += i
    return total