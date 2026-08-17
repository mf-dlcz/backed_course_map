'''
FIX LEVEL EXPERIENCE

The calculate_experience function should calculate the total experience earned across an inclusive range of character levels.

For each level:

- Earn level * 100 experience.

- Earn an additional 50 experience when the level is divisible by 3.

- Add that level's experience to the running total.

If start_level is greater than end_level, return 0.

The current function has mistakes in its loop boundaries, bonus condition, and running total.

'''

def calculate_experience(start_level, end_level):
    total_experience = 0

    for level in range(start_level, end_level + 1):
        # print(level, "level")
        level_experience = level * 100
        if level % 3 == 0:
            #print(level_experience, "BEFORE += 50")
            level_experience += 50
            #print(level_experience, "LEVEL EXPERIENCE")
        total_experience += level_experience

    return total_experience