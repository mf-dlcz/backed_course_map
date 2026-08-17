"""

Calculate Training Experience

Complete the calculate_training_xp function. 

It should calculate the total experience earned from start_level through end_level, including both endpoints.

For each level:

- Earn the level number multiplied by 8 experience.

- Earn 5 additional experience when the level number is divisible by 3.

- If start_level is greater than end_level, return 0.

Do not use collections or the built-in sum() function.

"""

def calculate_training_xp(start_level, end_level):
    total_xp = 0
    
    for level in range(start_level, end_level + 1):
        total_xp += level * 8
        if level % 3 == 0:
            total_xp += 5
        
        if start_level > end_level:
            return 0
            
    return total_xp