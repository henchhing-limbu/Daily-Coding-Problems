"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
"""

class OrdersRecoder:
	def __init__(self, N):
		self.max_size = N
		self.circular_buffer = [None] * self.max_size
		self.oldest_order_idx = 0

	def record(self, order_id):
		self.circular_buffer[self.oldest_order_idx] = order_id
		# When the index goes out of range, index is assigned 0.
		self.oldest_order_idx = (self.oldest_order_idx + 1) % self.max_size

	def get_last(self, i):
		return self.circular_buffer[self.oldest_order_idx - i]

orders_recoder = OrdersRecoder(5)
order_ids = [1, 2, 3, 4, 5]
for order_id in order_ids:
	orders_recoder.record(order_id)
print(orders_recoder.get_last(1))
orders_recoder.record(6)
orders_recoder.record(7)
print(orders_recoder.circular_buffer)
print(orders_recoder.get_last(3))

		
