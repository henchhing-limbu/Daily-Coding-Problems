"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

def count_unival_subtrees(root):
	if not root:
		return 1
	return count_unival_subtrees_helper(root)[1]

def count_unival_subtrees_helper(root):
	if not root:
		return (True, 0)
	left_info = count_unival_subtrees_helper(root.left)
	right_info = count_unival_subtrees_helper(root.right)

	# if both sides are unival trees
	if left_info[0] and right_info[0]:
		if root.left and root.right:
			if root.val == root.right.val and root.val == root.left.val:
				return (True, 1)
		elif root.right:
			return (False, right_infp[1])
		elif root.left:
			return (False, left_info[1])
		else:
			return (True, 1)
	# return sum of count of unival tress from both non-unival subtrees
	return (False, left_info[1] + right_info[1])
		

