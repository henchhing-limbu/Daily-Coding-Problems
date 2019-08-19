"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array execpt the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use divison?
"""
def product_array(nums):
	left_to_right_prod = [nums[0]]
	right_to_left_prod = [nums[-1]]
	length = len(nums)
	products = [0] * length
	for i in range(1, length - 1):
		left_to_right_prod.append(left_to_right_prod[i-1] * nums[i])
		right_to_left_prod.append(right_to_left_prod[i-1] * nums[-(i+1)])
	products[0] = right_to_left_prod[-1]
	products[-1] = left_to_right_prod[-1]
	for i in range(1, length - 1):
		products[i] = left_to_right_prod[i-1] * right_to_left_prod[-(i+1)]
	return products

print(product_array([1, 2, 3, 4, 5]))
print(product_array([3, 2, 1]))
print(product_array([1]))
print(product_array([5, 10]))
