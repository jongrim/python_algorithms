#! /usr/bin/python
import pdb
import random


def quicksort(items):
    # wrapper function

    def quicksort_helper(items, first, last):

        def partition(items, first, last):
            """Moves items to the right and left of the pivot and returns the position of the pivot"""
            if len(items) <= 1:
                # there is one or less items in the list, so return
                return items

            pivot = items[last]
            leftmark = first
            rightmark = last - 1

            # pdb.set_trace()

            finished = False

            while not finished:
                while items[leftmark] <= pivot and leftmark <= rightmark:
                    # will break when either the item is greater than the pivot, or leftmark has passed rightmark
                    leftmark += 1
                while items[rightmark] >= pivot and rightmark >= leftmark:
                    # will break when either the item is less than the pivot, or the rightmark has passed leftmark
                    rightmark -= 1

                if leftmark < rightmark:
                    items[leftmark], items[rightmark] = items[rightmark], items[leftmark]
                elif rightmark < leftmark:
                    items[leftmark], items[last] = items[last], items[leftmark]
                    finished = True

            return leftmark

        if first < last:
            splitpoint = partition(items, first, last)
            quicksort_helper(items, first, splitpoint - 1)
            quicksort_helper(items, splitpoint + 1, last)

    quicksort_helper(items, 0, len(items) - 1)

items = [random.randint(0, 1000) for i in range(100)]
quicksort(items)
print(items)