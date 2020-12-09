class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_iterative(self, value):
        curr =  self.root
        while True:
            if value > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(value)
                    break      
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(value)
                    break  
                

    def insert_recursive(self, curr, value):
        if curr.value < value:
            if curr.right:
                self.insert_recursive(curr.right, value)
            else:
                curr.right = Node(value)   
        else:
            if curr.left:
                self.insert_recursive(curr.left, value)
            else:
                curr.left = Node(value) 


    def insert_recursive_helper(self, value):
        self.insert_recursive(self.root, value)

    def search_recursive_helper(self, value):
        return self.search_recursive(self.root, value) 

    def search_recursive(self, curr, value):
        if curr:
            if curr.value == value:
                return True
            elif curr.value < value:
                return self.search_recursive(curr.right, value)
            elif curr.value > value:
                return self.search_recursive(curr.left, value)                  
        else:
            return False    


bst = BST(10)
bst.insert_recursive_helper(3)
bst.insert_recursive_helper(2)
bst.insert_recursive_helper(6)
bst.insert_iterative(7)
bst.insert_iterative(8)
bst.insert_iterative(9)
bst.insert_iterative(123)


print("Search - "+ str(bst.search_recursive_helper(0)))

