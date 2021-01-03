class Stack():
    def __init__(self):
    	self.stack = []

    def push(self, val):
    	self.stack.append(val)

    def pop(self):
    	self.stack.pop()

    def print_stack(self):
    	return self.stack

    def is_empty(self):
    	return self.stack == []

    def peek(self):
    	if not self.is_empty():
    		return self.stack[-1]
    	else:
    		return "Cannot peek an empty stack!"

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(6)
print(stack.print_stack())
print(stack.peek())
stack.pop()
print(stack.print_stack())
