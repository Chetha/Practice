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
