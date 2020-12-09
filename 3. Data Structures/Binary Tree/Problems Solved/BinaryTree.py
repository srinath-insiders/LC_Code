class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorderTraversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorderTraversal(start.left, traversal)
            traversal = self.preorderTraversal(start.right, traversal)
        return traversal     

    def inorderTraversal(self, start, traversal):
        if start:
            traversal = self.inorderTraversal(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.inorderTraversal(start.right, traversal)
        return traversal     

    def postorderTraversal(self, start, traversal):
        if start:
            traversal = self.postorderTraversal(start.left, traversal)
            traversal = self.postorderTraversal(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal             

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)        

print(tree.preorderTraversal(tree.root, ""))
print(tree.inorderTraversal(tree.root, ""))
print(tree.postorderTraversal(tree.root, ""))
