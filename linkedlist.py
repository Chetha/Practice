class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_linkedlist(self):
		curr_node = self.head

		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next

	#INSERTION
	#inserting at end of linked list
	def append(self, data):
		new_node = Node(data)

		#if the list is empty
		if self.head is None:
			self.head = new_node
			return

		# Else, create curr_node and assign to head
		curr_node = self.head

		#iterating till you are at the last node means that you assign curr_node to NULL
		#so the next step of assigning curr_node's next to new_node won't work
		# A - B - C - None <- this None is what curr_node will be pointing to
		# To get to the last node, iterate till curr_node next is None
		while curr_node.next:
			curr_node = curr_node.next

		#append last element's next to the new node
		curr_node.next = new_node

	#inserting at the start
	def prepend(self, data):
		new_node = Node(data)
		#if list is empty
		if not self.head:
			self.head = new_node
		# B - C, new_node = A and head = B
		# A.next = B
		new_node.next = self.head
		#now reassign head to the prepended new_node
		self.head = new_node

	#inserting after node
	def insert_after_node(self, prev_node, data):
		
		# just took it out the video, this case will almost never happen considering the way 
		# the prev_node is fed into the function
		if not prev_node:
			print("Previous node not in list")
			return 
		#first, create new_node as always
		new_node = Node(data)
		# A - C
		#   B
		# B.next = A.next (which is C), assign first to not lose C and nodes after that
		new_node.next = prev_node.next
		# A.next = B
		prev_node.next = new_node

	#DELETION
	#Deletion cases - 1. Node to be deleted is head, 2. Node to be deleted is not head
	def delete_node(self, key):
		curr_node = self.head
		# if list is not empty, that is, there is a head, and head's data == key
		if curr_node and curr_node.data == key:
			# A = key, A - B - C
			# self.head = A.next
			self.head = curr_node.next
			# # del A
			# del curr_node
			# or curr_node = None removes the head
			curr_node = None
			return 

		#for case 2, we need to know the prev node as well
		prev = None
		# A - B - C, B = key
		# Iterate to the node before the node to be deleted for prev
		# curr_node would be the node to be deleted
		while curr_node and curr_node.data != key:
			prev = curr_node
			curr_node = curr_node.next

		#if cur_node is none, return, that is, if we have iterated the entire
		#list and the key is not found, return none
		if curr_node is None:
			return
		#A.next = B.next
		prev.next = curr_node.next 
		# B = None
		curr_node = None


linkedlist = LinkedList()
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("D")
#linkedlist.print_linkedlist()
linkedlist.prepend("E")
#linkedlist.print_linkedlist()
linkedlist.insert_after_node(linkedlist.head.next.next, "C")
linkedlist.print_linkedlist()
print("\n")

#testing case 1 of deletion
linkedlist.delete_node(linkedlist.head.data)
linkedlist.print_linkedlist()
print("\n")

#testing case 2
linkedlist.delete_node(linkedlist.head.next.data)
linkedlist.print_linkedlist()
print("\n")

