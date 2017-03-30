#! /usr/bin/env python


def selection_sort(to_sort):

    def get_smallest(to_search):
        min = to_search[0]
        index = 0
        for i in to_search:
            if i < min:
                index = to_search.index(i)
                min = i
        return index

    offset = 0
    for i in to_sort:
        i_index = to_sort.index(i)
        min = offset + get_smallest(to_sort[to_sort.index(i):])
        to_sort[i_index], to_sort[min] = to_sort[min], to_sort[i_index]
        offset += 1


unsorted = [3, 78, 32, 15, 66, 23, 9, 27]
selection_sort(unsorted)
print(unsorted)
