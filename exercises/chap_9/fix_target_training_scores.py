"""

FIX TARGET TRAINING SCORES

The get_target_scores function should build and return a new list containing only the daily training 
scores that meet or exceed minimum_target.

The current loop, condition, and appended value are incorrect. 

Fix them using a loop, an if statement, and .append().

Preserve the scores' original order.

Include scores equal to the minimum target.

Return an empty list when no scores qualify or the input list is empty.

"""

def get_target_scores(daily_scores, minimum_target):
    target_scores = []
    
    for score_index in range(len(daily_scores)):
        if daily_scores[score_index] >= minimum_target:
            target_scores.append(daily_scores[score_index])
    return target_scores