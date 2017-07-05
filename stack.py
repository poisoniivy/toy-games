"""Implementing Stack class using lists."""

class Stack(object):

	def __init__(self):
		self._items = [] #don't forget "_" in front of variable only used in class that is not externally accessed

	def is_empty(self): #python 3 isEmpty, python2 -> is_empty
		return self._items == []

	def push(self, item):
		self._items.append(item)

	def pop(self): #watch out for arguments, don't forget self as argument
		return self._items.pop()

	def peek(self):
		# return self._items[len(self._items) -1]
		return self._items[-1]

	def size(self):
		return len(self._items)

	def print_stack(self):
		print self._items


""" Using Stack class to convert decimal to binary."""

def decimal_to_binary(decimal):
	"""
	>>> decimal_to_binary(123)
	1111011
	"""
	bin_stack = Stack()

	while decimal != 0:
		digit = decimal % 2
		bin_stack.push(digit)
		decimal = decimal / 2

	# bin_stack.print_stack()
	binary_num = ""

	while not bin_stack.is_empty():
		# Note: When you pop, it comes out as a number. Need to convert to string to add to binary_num string
		binary_num = binary_num + str(bin_stack.pop()) 

	print binary_num


def are_parens_balanced(symbols):
	""" Return T/F if parentheses are balanced in an expression."""

	parens = Stack() # creates stack

	for char in symbols:

		if char == "(":
			parens.push(char)

		elif char == ")":
			if parens.is_empty():
				return False
			else:
				parens.pop()

	return parens.is_empty()