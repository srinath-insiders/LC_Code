class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def size_of_a_tree(self, node):
        if not node:
            return 0
        left = self.size_of_a_tree(node.left)
        right = self.size_of_a_tree(node.right)

        return 1 + left + right
            

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)   

print(tree.size_of_a_tree(tree.root))
