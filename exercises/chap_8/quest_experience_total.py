"""
QUEST EXPERIENCE TOTAL

Complete the calculate_quest_xp function.

It should calculate the total experience earned from start_level through end_level, including both endpoints.

For each level:

- Levels divisible by 5 award 50 XP

- Other even levels award 20 XP

- Odd levels award 10 XP

- Check divisibility by 5 first. If start_level is greater than end_level, return 0.

"""

def calculate_quest_xp(start_level, end_level):
    total_xp = 0
    if start_level > end_level:
        return 0
    for level in range(start_level, end_level + 1):
        if level % 5 == 0:
            total_xp += 50
        elif level % 2 == 0:
            total_xp += 20
        elif level % 2 == 1:
            total_xp += 10
    return total_xp