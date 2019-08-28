"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# TODO(henxing): Implement the system using Trie data structure
class Node:
	def __init__(self, val):
		self.val = val
		self.children = [None] * 26

class AutoCompleteSystem:
	def __init__(self, possible_query_strs):
		self.possible_query_strs = possible_query_strs
		self.start_nodes = [None] * 26

	def preprocess_query_strs(self):
		# go through each word 
		for query_str in self.possible_query_strs:
			nodes = self.start_nodes
			# go through each character of the word
			for char in query_str:
				# Populate the trie with the characters
				# get the position of the char in the list
				i = ord(char) - 97
				print('Value of i is: {}' .format(i))
				# make a Node object of that char if it does not exist already
				if nodes[i] is None:
					nodes[i] = Node(char)
				# make the nodes to be its children nodes.
				nodes = nodes[i].children

	def get_possible_strings(self, query_str):
		# get the list of start nodes of suffixes that has query_str as prefix
		nodes = self.start_nodes
		for char in query_str:
			node = nodes[ord(char) - 97]
			if node is None:
				return []
			nodes = node.children
		possible_str = [query_str + suffix for suffix in self.get_possible_suffixes(node.children)]
		return possible_str	
		
	
	def get_possible_suffixes(self, nodes):
		if all(node is None for node in nodes):
			return ['']
		suffixes = []
		for node in nodes:
			if node:
				child_suffixes = self.get_possible_suffixes(node.children)
				for child_suffix in child_suffixes:
					suffixes.append(node.val + child_suffix)
		return suffixes
				
	

autocomplete_sys = AutoCompleteSystem(['dog', 'deer', 'deal', 'henchhing'])
autocomplete_sys.preprocess_query_strs()
print(autocomplete_sys.get_possible_strings('de'))
