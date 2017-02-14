#! /usr/bin/env python
import random

def merge_sort(unsorted_items):
    if len(unsorted_items) < 2:
        return unsorted_items
    
    elif len(unsorted_items) > 2:
        merge_list_a = merge_sort(unsorted_items[:len(unsorted_items)//2])
        merge_list_b = merge_sort(unsorted_items[len(unsorted_items)//2:])
    
    else:
        if unsorted_items[0] > unsorted_items[1]:
            unsorted_items[0], unsorted_items[1] = unsorted_items[1], unsorted_items[0]
            return unsorted_items
        else:
            return unsorted_items

    final_merge = []

    while merge_list_a and merge_list_b:
        if merge_list_a[0] < merge_list_b[0]:
            final_merge.append(merge_list_a[0])
            merge_list_a.pop(0)
        else:
            final_merge.append(merge_list_b[0])
            merge_list_b.pop(0)
    if len(merge_list_a) > 0:
        for item in merge_list_a:
            final_merge.append(item)
    elif len(merge_list_b) > 0:
        for item in merge_list_b:
            final_merge.append(item)

    return final_merge

rand_gen = (random.randint(1, 100) for x in range(20))
unsorted_list = [x for x in rand_gen]
print(merge_sort(unsorted_list))
