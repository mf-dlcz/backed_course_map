"""

SORT RIDERS INTO TWO CARS:

Complete the split_riders function.

A roller coaster loads riders into two cars by alternating between them. The first rider goes into car one, the second goes into car two, the third goes into car one, and so on.

Use a for loop to process the list. Return a list containing the two car lists in this order:

- Car one
- Car two

If the input list is empty, both car lists should be empty.

For example:

riders = ["Ari", "Bo", "Cleo", "Dev", "Eli"]
print(split_riders(riders))
# [["Ari", "Cleo", "Eli"], ["Bo", "Dev"]]

"""

def split_riders(riders):
    car_one = []
    car_two = []

    for rider in range(len(riders)):
        if rider % 2 == 0:
            car_one.append(riders[rider])
        else:
            car_two.append(riders[rider])
    return [car_one, car_two]