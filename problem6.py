"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

# Note: This class assumes the implementation of get_pointer() and
#       dereference_pointer() functions.
class Node:
	def __init__(self, val):
		self.val = val
		self.both = 0


class LinkedList:
	def __init__(self, val):
		self._head = Node(val)
		
		
	def add(self, val):
		curr_node = self._head
		prev_node_ptr = 0
		# For the last node of the linked list, the XOR value is simply going
		# to te the pointer of the last node as ptr XOR 0 is ptr.
		while get_pointer(curr_node) == curr_node.both:
			next_node_ptr = curr_node.both ^ prev_node_ptr
			prev_node_ptr = get_pointer(curr_node)
			curr_node = dereference_pointer(next_node_ptr)
		# Create node and add to the end of the linked list.
		new_node = Node(val)\
		new_node.both = get_pointer(curr_node)
		curr_node.both = curr_node.both ^ get_pointer(new_node)

	def get(index):
		# TODO(henxing): Just need to add count to add() logic. Implement this
		#				 method when you have time.
		pass
		
		

		
			
