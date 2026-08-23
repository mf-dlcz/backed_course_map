"""

BUILDING TRENDING REWARDS

Complete the build_training_rewards function.

It should loop from start_step up to, but not including, stop_step. 

For each step, calculate its reward by multiplying the step number by points_per_step, then 
append the reward to a list.

Return the completed list. If the range is empty, return an empty list.

"""

def build_training_rewards(start_step, stop_step, points_per_step):
    rewards = []
    
    for step in range(start_step, stop_step):
        reward = step * points_per_step
        rewards.append(reward)
    return rewards