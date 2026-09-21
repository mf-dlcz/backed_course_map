"""
FIX CHECKPOINT UPDATES:

The update_checkpoint function receives:

- A checkpoint tuple containing its name, x-coordinate, and y-coordinate

- Changes to apply to both coordinates

- A new checkpoint name

- It should return a new three-item tuple in this order:

The new name
The updated x-coordinate
The updated y-coordinate
The current function creates the wrong tuple shape and does not update both coordinates correctly.

Example
- checkpoint = ("Gate", 4, 7)
- update_checkpoint(checkpoint, 3, -2, "North Gate")
# ("North Gate", 7, 5)

Do not change the original checkpoint tuple.

"""

def update_checkpoint(checkpoint, x_change, y_change, new_name):
    name, x, y = checkpoint
    return (new_name, (x + x_change), (y + y_change))