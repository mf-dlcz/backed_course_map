"""
FIX TOWER ENERGY LEVEL

The calculate_tower_energy function should total the energy earned across every level from 
start_level through end_level, including both endpoints.

Each level awards energy according to the first matching rule:

- Levels divisible by 5 award three times the level number.

- Other even levels award twice the level number.

- Odd levels award the level number.

- If start_level is greater than end_level, return 0.

The current function has problems with its accumulator, range boundary, and branching. Fix it without changing the function name or parameters.

"""

def calculate_tower_energy(start_level, end_level):
    total_energy = 0
    if start_level > end_level:
        return 0
        
    for level in range(start_level, end_level + 1):
        if level % 5 == 0:
            total_energy += level * 3
        elif level % 2 == 0:
            total_energy += level * 2
        else:
            total_energy += level

    return total_energy