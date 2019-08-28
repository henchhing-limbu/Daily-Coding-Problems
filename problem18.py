"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""
from collections import deque
def get_max_values(nums, k):
	max_values = []
	sliding_window = deque()
	# Creating sliding window for first k integers.
	for i in range(k):
		while sliding_window:
			if nums[sliding_window[-1]] > nums[i]:
				break
			sliding_window.pop()
		sliding_window.append(i)
	max_values.append(nums[sliding_window[0]])

	for i in range(k, len(nums)):
		max_int_idx = sliding_window[0]
		if i >= max_int_idx + k: # The max int is not in current window.
			sliding_window.popleft()

		while sliding_window:
			# break out of the loop if all the ints in window are > than curr int.
			if nums[sliding_window[-1]] > nums[i]:
				break
			sliding_window.pop()
		sliding_window.append(i)
		max_values.append(nums[sliding_window[0]])

	return max_values
		
	
print(get_max_values([10, 5, 2, 7, 8, 7], 3))
