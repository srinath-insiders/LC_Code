class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def height_of_a_binarytree(self, node):
        if not node:
            return -1
        leftSubtreeHeight = self.height_of_a_binarytree(node.left)
        rightSubtreeHeight = self.height_of_a_binarytree(node.right)

        return 1 + max(leftSubtreeHeight, rightSubtreeHeight)





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)     

print(tree.height_of_a_binarytree(tree.root))