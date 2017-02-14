#! /usr/bin/env python
import random

def insertion_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list

    j = 1
    while j < len(unsorted_list):
        key = unsorted_list[j]
        i = j - 1

        while i >= 0 and unsorted_list[i] > key:
            unsorted_list[i+1] = unsorted_list[i]
            i -= 1

        unsorted_list[i+1] = key
        j += 1

    return unsorted_list

rand_gen = (random.randint(1, 100) for x in range(20))
unsorted_list = [x for x in rand_gen]
print(insertion_sort(unsorted_list))
