"""

MEDICATION SESSION

Complete the meditate function. It should simulate attempts to complete calming breaths.

The function receives:

- target_calm: the calm score needed to finish

- session_limit: the maximum number of breath attempts

- interrupted_every: every numbered breath that is interrupted

- Each uninterrupted breath increases the calm score by 1. Interrupted breaths still count as attempts but do not increase the calm score.

Return the total number of breath attempts when the target is reached or the session limit expires.

Requirements:

- Use a while loop.

- Use continue to ignore interrupted breaths.

- Use break as soon as the target calm score is reached.

- If interrupted_every is 0, no breaths are interrupted.

- If the target is 0 or less, return 0.

"""

def meditate(target_calm, session_limit, interrupted_every):
    attempts = 0
    calm_score = 0
    
    if target_calm <= 0:
        return 0
    
    while attempts < session_limit:
        attempts += 1
        if interrupted_every > 0 and attempts % interrupted_every == 0:
            continue
        
        calm_score += 1
        
        if calm_score >= target_calm:    
            break
            
    return attempts