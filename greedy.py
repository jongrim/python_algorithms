"""
A simple demonstration of implementing a greedy algorithm. When determining
if an item should be taken or not, check if there is room for the item based
on whatever quantitative measure is being used. If there is, take it, if not,
leave it behind.
"""


def greedy(items, max_cost, key_function):
    """
    Assumes items is a list, max_cost >= 0, and key_function returns a
    numerical value of relevance for the item and desired sorting
    """
    items_copy = sorted(items, key=key_function, reverse=True)

    result = []
    total_value, total_cost = 0.0, 0.0

    # Assumes each item has a value and cost attribute
    for i in items_copy:
        if i.cost <= (max_cost - total_cost):
            result.append(i)
            total_value += i.value
            total_cost += i.cost

    return (result, total_value, total_cost)
