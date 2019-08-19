"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
def two_numbers(nums, k):
	diffs = set()
	for num in nums:
		if num in diffs:
			return True
		diffs.add(k - num)
	return False

print(two_numbers([1, 5, 9, 10], 11))
print(two_numbers([1, 3, 2, 12], 11))
