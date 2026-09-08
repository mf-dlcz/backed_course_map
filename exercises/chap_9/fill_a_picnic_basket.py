"""

FILL A PICNIC BASKET

Complete the fill_picnic_basket function.

It receives a list named basket and three foods. Use .append() to add each food to the end of the basket in the same order they are given. Then return the basket.

For example:

basket = ["blanket"]
result = fill_picnic_basket(basket, "sandwiches", "apples", "juice")
print(result)
# ["blanket", "sandwiches", "apples", "juice"]

Your function must also work when basket starts empty.

"""

def fill_picnic_basket(basket, first_food, second_food, third_food):
    basket.append(first_food)
    basket.append(second_food)
    basket.append(third_food)
    return basket