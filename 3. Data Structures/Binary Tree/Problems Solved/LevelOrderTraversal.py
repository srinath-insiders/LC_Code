from Queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def level_order_traversal(self, root):
        queue = Queue()
        queue.enqueue(root)

        traversal = ""
        while not queue.is_empty():
            node = queue.dequeue()
            traversal += (str(node.value) + "-")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal        





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)     

print(tree.level_order_traversal(tree.root))


