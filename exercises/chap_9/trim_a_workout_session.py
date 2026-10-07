"""

TRIM A WORKOUT SESSION:

Complete the trim_session function.

It receives:

- A list of workout activities

- The number of warm-up activities at the beginning

- The number of cooldown activities at the end

Use list slicing to return a new list containing only the main workout activities.

For example:

activities = ["walk", "stretch", "squat", "push-up", "jog"]
print(trim_session(activities, 2, 1))
# ["squat", "push-up"]

The original list should not be changed. Either count may be 0.

"""

def trim_session(activities, warmup_count, cooldown_count):
    stop = len(activities) - cooldown_count
    
    return activities[warmup_count:stop]