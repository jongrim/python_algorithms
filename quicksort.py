#! /usr/bin/python
import random


def quicksort(items):
    # wrapper function

    def quicksort_helper(items, first, last):

        def partition(items, first, last):
            """
            Moves items to the right and left of the pivot and returns the
            position of the pivot
            """
            if len(items) <= 1:
                # there is one or less items in the list, so return
                return items

            pivot = items[last]
            left = first
            right = last - 1

            finished = False

            while not finished:
                while items[left] <= pivot and left <= right:
                    left += 1
                while items[right] >= pivot and right >= left:
                    right -= 1

                if left < right:
                    items[left], items[right] = items[right], items[left]
                elif right < left:
                    items[left], items[last] = items[last], items[left]
                    finished = True

            return left

        if first < last:
            splitpoint = partition(items, first, last)
            quicksort_helper(items, first, splitpoint - 1)
            quicksort_helper(items, splitpoint + 1, last)

    quicksort_helper(items, 0, len(items) - 1)


items = [random.randint(0, 1000) for i in range(100)]
quicksort(items)
print(items)
