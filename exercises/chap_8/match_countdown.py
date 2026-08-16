"""
Match Countdown

Complete the countdown_to_start function.

1. Write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:
    10...
    9...
    8...
    etc.

2. However, when i is 1, print "Fight!" on the same line:
    1...Fight!

"""

def countdown_to_start():
    for i in range(10, 0, -1):
        if i == 1:
            print("1...Fight!")
        else:
            print(f"{i}...")