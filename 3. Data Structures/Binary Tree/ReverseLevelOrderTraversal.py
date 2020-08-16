class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0,data)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)       

    def isEmpty(self):
        return self.size() == 0

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)       

    def isEmpty(self):
        return self.size() == 0        

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        if start:
            traversal += "-"+ str(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal = traversal +"-"+ str(start.value)    
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal +"-"+ str(start.value) 
            traversal = self.inorder_print(start.right, traversal)
        return traversal   

    def levelorder_print(self, start):
        traversal = ""
        if start:
            queue = Queue()
            queue.enqueue(start)
            while queue.size() > 0:
                node = queue.dequeue()
                traversal += str(node.value) + "-"

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        return traversal  

    def reverseLevelorderTraversal_print(self, start):
        terversal = ""
        if start:
            queue = Queue()
            stack = Stack()

            queue.enqueue(start)

            while queue.size() > 0:
                node = queue.dequeue()
                stack.push(node.value)

                if node.right:
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)

            while stack.size() > 0:
                terversal += str(stack.pop()) + "-"     

            return terversal           





    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root,"")
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root,"")                
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root,"")
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root)
        elif traversal_type == 'reverselevelorder':
            return self.reverseLevelorderTraversal_print(self.root)        
        else:
            return 'Traversal type '+traversal_type+' is not supported'            


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(9)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('reverselevelorder')) 