"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def longest_substr(s, k):
	if len(s) < k:
		return ''
	# Start index of current susbtring
	substr_start = 0
	# Index used to keep track of longest susbstring
	longest_substr_start, longest_substr_end = 0, 0
	# List with index as ord(char) and values as their count.
	# Need to keep track of char's last index.
	seen_chars = [-1] * 26
	# Keeps track of number of unique characters seen.
	unique_chars_count = 0
	
	for idx in range(len(s)):
		char = s[idx]
		asci_val = ord(char) - 97
		if seen_chars[asci_val] > -1:  # update index to latest index of the char
			seen_chars[asci_val] = idx
		else:
			seen_chars[asci_val] = idx
			unique_chars_count += 1
			if unique_chars_count > k:
				# check if curr substring is longer than global susbtr
				if longest_substr_end - longest_substr_start < idx - substr_start:
					longest_substr_start = substr_start
					longest_substr_end = idx
				# Update the seen chars array and get the new start index.
				substr_start = _update_seen_chars(seen_chars, ord(s[idx-1]) - 97)
	idx += 1
	if longest_substr_end - longest_substr_start < idx - substr_start:
		longest_substr_start = substr_start
		longest_substr_end = idx

	return s[longest_substr_start: longest_substr_end]
		

def _update_seen_chars(seen_chars, i):
	idx = seen_chars[i]
	for j in range(len(seen_chars)):
		if seen_chars[j] < idx:
			seen_chars[j] = 0
	# find the new start index
	new_start_idx = float('inf')
	for index in seen_chars:
		if -1 < index < new_start_idx:
			new_start_idx = index
	return new_start_idx

print(longest_substr('abcba', 2))
print(longest_substr('', 2))		
print(longest_substr('aaabbbccc', 3))	
