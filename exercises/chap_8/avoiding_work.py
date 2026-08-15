"""
Avoiding Work

Fix the award_enchantments function. It calculates the strength of the enchantment – 5 times the total number of quests completed – and prints a message for the player. But we need to make sure this happens only once for every three quests that we iterate over within the loop! Only count the quests in the loop, don't worry about the total number of quests being divisible by 3.

1. At the beginning of the function, before the loop, initialize a counter variable to 0.

2. Within the for loop:

    1. Add 1 to counter in each iteration, to keep track of how many quests we've seen.

    2. If counter is less than 3, continue to the next iteration.

    3. Otherwise, we must have completed 3 quests! Reset counter to 0 before the enchantment is awarded.

"""

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        enchantment_strength = quest_number * 5
        counter += 1

        if counter < 3:
            continue
        else:
            counter = 0
        
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )