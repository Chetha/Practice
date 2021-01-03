#Using list, FIFO
#Check collection.dequeue 
#at this article https://levelup.gitconnected.com/stacks-and-queues-in-python-b2e8b4dbd876

class Queue():
	def __init__(self):
		self.queue = []

	def enqueue(self, val):
		self.queue.append(val)

	def is_empty(self):
		return self.queue == []

	def print_queue(self):
		return self.queue

	def dequeue(self):
		if not self.is_empty():
			return self.queue.pop(0)
		else:
			return None

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")
print(queue.print_queue())
queue.dequeue()
print(queue.print_queue())

