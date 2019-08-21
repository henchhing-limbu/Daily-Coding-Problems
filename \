"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
def first_missing_positive_int(array):
	size = len(array)
	# start index of the subarray of positive integers.
	start_idx = _partition_pos_neg(array)
	# if there are no positive integers in the array
	if start_idx == size:
		return 1
	pos_array_size = size - start_idx
	for i in range(start_idx, size):
		# This needs to be absolute as traversing from left to right, the if
		# statement below might convert the array element on right side of
		# current iteration to it's negative value. The converted negative
		# could be the smallest positive integer.
		num = abs(array[i])
		if num - 1 < pos_array_size and array[start_idx + (num - 1)] > 0:
			array[start_idx + num - 1] = - array[start_idx + (num - 1)]

	# go through positive subarray to find index with +ve element.
	for i in range(start_idx, size):
		if array[i] > 0:
			return (i - start_idx) + 1
	return (i - start_idx) + 1
	

def _partition_pos_neg(array):
	"""Separates negative and positive numbers and returns the index."""
	i = 0
	for j in range(len(array)):
		if array[j] < 1:
			array[i], array[j] = array[j], array[i]
			i += 1
	return i

print(first_missing_positive_int([0, 10, 2, -10, -20]))
print(first_missing_positive_int([3, 4, -1, 1]))
print(first_missing_positive_int([1, 2, 0, 3]))
print(first_missing_positive_int([-1, -2, -3, -4]))
print(first_missing_positive_int([]))

