"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def largest_sum_of_non_adj_nums(nums):
	if not nums:
		return 0
	incl = nums[0]
	excl = 0
	for i in range(1, len(nums)):
		new_incl = max(incl, excl + nums[i])
		excl = incl
		incl = new_incl
	return max(incl, excl)

print(largest_sum_of_non_adj_nums([2, 4, 6, 2, 5]))
print(largest_sum_of_non_adj_nums([5, 1, 1, 5]))
print(largest_sum_of_non_adj_nums([]))
