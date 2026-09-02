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

def build_inventory_labels(item_names, copy_count):
    labels = []

    if copy_count <= 0:
        return labels

    for item_index in range(len(item_names)):
        item_name = item_names[item_index]
        labels.append(item_name)

        for copy_number in range(1, copy_count + 1):
            labels.append(f"{item_name}-{copy_number}")

    return labels