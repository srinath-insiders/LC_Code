from Queue import Queue
from stack import Stack

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def reverse_level_order_traversal(self, root):
        queue = Queue()
        queue.enqueue(root)
        stack = Stack()
       
        while not queue.is_empty():
            node = queue.dequeue()
            stack.push(node.value)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while not stack.is_empty():
            print(stack.pop())



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)     

print(tree.reverse_level_order_traversal(tree.root))


