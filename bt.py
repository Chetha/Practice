class Queue(object):
    def __init(self):
        self.items = []

    def enqueue(self, items):
        self.items.insert(0, item)
    '''
    From terminal -
    >>> nums = [1]
    >>> num = 3
    >>> nums.insert(0, num)
    >>> print(nums)
    [3, 1]
    '''
    #we peek the last element of list and when we insert both left and right children
    #into list, we insert left child first at index 0 and then right child at index 0
    #The above snippet shows that when right child is added to list at index 0, the
    #previous left child value gets pushed to the next position, which is why we use
    #self.items[-1].value to peek(we get the last element of list(the left child))
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self, items):
        return len(self.items) == 0

    def peek(self, items):
        if not self.is_empty():
            return self.items[-1].value


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def printTraversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        else:
            print("Traversal type " + traversal_type + "is not supported")
            return False


    def preorder(self, start, traversal):
        "root -> left -> right"
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        "left -> root -> right"
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        "left -> right -> root"
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

#level 1
tree = BinaryTree(1)

#level 2
tree.root.left = Node(2)
tree.root.right = Node(3)

#level 3
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#level 4
tree.root.left.left.left = Node(8)

print(tree.printTraversal("preorder")) #O/P -> 1-2-4-8-5-3-6-7-
print(tree.printTraversal("inorder")) #O/P -> 8-4-2-5-1-6-3-7-
print(tree.printTraversal("postorder")) #O/P -> 8-4-5-2-6-7-3-1-
