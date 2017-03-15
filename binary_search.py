#! /usr/bin/python

"""
Binary search will search through a sorted group of items and return the
desired item. This is achieved by seperating the group of items in half and
determining if the item is greater than or less than the mid-point. By
doing such, the search space is reduced by half with every search.
"""


def binary_search(items, e):
    """Determine the place of e within items, and return this location"""
    def binary_search_helper(low, high, e):
        mid = (high + low) // 2
        if items[mid] == e:
            return mid
        elif items[mid] < e:
            return binary_search_helper(mid, high, e)
        else:
            return binary_search_helper(low, mid, e)

    return binary_search_helper(0, len(items) - 1, e)


nums = [2**x for x in range(20)]
print(binary_search(nums, 128))  # prints 7, i.e. 2^8
