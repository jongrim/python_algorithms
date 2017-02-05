#! python


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


print(insertion_sort([5, 2, 3, 1, 4]))
print(insertion_sort([55, 50, 45, 40, 35, 20, 15, 10, 5, 3, 100]))
print(insertion_sort([1, 2, 3, 4, 5]))
