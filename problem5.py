"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(fun):
	def first_element(a, b):
		return a
	return fun(first_element)

def cdr(fun):
	def last_element(a, b):
		return b
	return fun(last_element)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))


