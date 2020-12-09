class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        else:
            newNode = Node(data)
            newNode.next = prev_node.next
            prev_node.next = newNode        

    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        else:
            while curr_node.next:
                previous_node = curr_node
                curr_node =  curr_node.next
                if curr_node.data == key:
                    previous_node.next = curr_node.next
                    curr_node = None
                    return
    def delete_node_at_position(self, pos):
        curr_node = self.head

        if curr_node and pos == 0:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        count = 0
        while curr_node and count != pos:
            prev = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node.next == None:
            return

        prev.next =  curr_node.next
        curr_node = None        

    def len_iterative(self):
        curr_node = self.head
        count = 0
        while curr_node:
            curr_node = curr_node.next
            count += 1
        return count

    def recursive_length(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)


    def print_linkedList(self):
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next     
            
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next    

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)   

    def reverse_iterative(self):

        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        self.head = prev            


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")
llist.delete_node("E")
llist.delete_node_at_position(0)

llist.prepend("B")
llist.prepend("A")
llist.swap_nodes("A","D")
llist.print_linkedList()
print("--------------------")
llist.reverse_recursive()
llist.print_linkedList()

print("Iterative Length - "+str(llist.len_iterative()))
print("Recursive Length - "+str(llist.recursive_length(llist.head)))


