"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

mapping = {}
char = 'a'
for i in range(1, 27):
	mapping[str(i)] = char
	char = chr(ord(char) + 1)

def get_num_of_decoded_messages(message, mapping):
	 return _get_num_of_decoded_messages_helper(message, 0)

def _get_num_of_decoded_messages_helper(message, i):
	if i >= len(message):
		return 1
	if message[i] == '0':
		return 0
	if i + 1 < len(message):
		return _get_num_of_decoded_messages_helper(message, i+1) + _get_num_of_decoded_messages_helper(message, i+2)
	return _get_num_of_decoded_messages_helper(message, i+1)
print(get_num_of_decoded_messages('1', mapping))
print(get_num_of_decoded_messages('111', mapping))
print(get_num_of_decoded_messages('1021', mapping))
print(get_num_of_decoded_messages('1221', mapping))

