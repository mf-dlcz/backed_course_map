"""

Fixes the number of inventory labels in the system.

The build_inventory_labels function should build a new list of labels for each item name.

For every item, append:

The original item name
The requested number of numbered copies, starting at 1
For example:

build_inventory_labels(["rope", "torch"], 2)
# ["rope", "rope-1", "rope-2", "torch", "torch-1", "torch-2"]

The current function has incorrect loop bounds and appends the wrong value for numbered copies. Fix it using loops, list indexing, and .append().

Return an empty list when:

The input list is empty
copy_count is zero or negative

"""

