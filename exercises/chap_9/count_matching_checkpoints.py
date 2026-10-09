"""

Count Matching Checkpoints:

Complete the count_matching_checkpoints function.

It receives two lists of checkpoint names. 

Count how many checkpoints are the same at the same index in both lists.

Use a for loop to compare the lists. 

Only compare indexes that exist in both lists. 

Do not use sets.

"""

def count_matching_checkpoints(planned, visited):
    counter = 0

    if len(planned) < len(visited):
        run = len(planned)
    else:
        run = len(visited)
    
    for trips in range(run):
        if planned[trips] == visited[trips]:
            counter += 1
    return counter