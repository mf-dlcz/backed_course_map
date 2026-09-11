"""
Find the Busiest Arcade Hour

Complete the find_busiest_hour function.

It receives a non-empty list containing the number of players at an arcade during each hour. Return the largest number in the list.

Use a loop and comparison operators. Do not use Python's built-in max function.

For example:

player_counts = [12, 27, 19, 34, 22]
print(find_busiest_hour(player_counts))
# 34

The list may contain one number, and its numbers may be negative.

"""

def find_busiest_hour(player_counts):
    max_num_players= float("-inf")

    for player in player_counts:
        if player > max_num_players:
            max_num_players = player
    return max_num_players