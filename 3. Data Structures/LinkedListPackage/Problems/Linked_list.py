class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self,node, data):
        curr = self.head
        newNode = Node(data)

        while curr:
            if curr.data == node.data:
                newNode.next = curr.next
                curr.next = newNode
            curr = curr.next    

    def deletion_by_value(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        while curr and curr.next:
            prev = curr
            curr = curr.next

            if curr.data == data:
                prev.next = curr.next

    def deletion_by_position(self, pos):
        if pos == 0 and self.head:
            self.head = self.head.next
        
        curr = self.head
        prev = None
        position = 0
        while curr and curr.next:
            prev = curr
            curr = curr.next
            position += 1

            if position == pos:
                prev.next = curr.next

    def length_iterative(self):
        length = 0
        curr = self.head

        while curr:
            length += 1
            curr = curr.next
        print("Length - "+str(length)) 

    def length_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.length_recursive(node.next)    

    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head

        while curr1:
            if curr1.data == key1:
                break
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        
        while curr2:
            if curr2.data == key2:
                break
            prev2 = curr2
            curr2 = curr2.next


        if not curr1 or not curr2:
            return

        if prev1 is None:
            self.head = curr2
        else:
            prev1.next = curr2

        if prev2 is None:
            self.head = curr1
        else:
            prev2.next = curr1


        curr1.next, curr2.next = curr2.next, curr1.next 

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def merge_two_sorted_list(self, list2):
        
        p = self.head
        q = list2.head
        s = LinkedList()


        while p and q:
            
            if p.data <= q.data:
                s.append(p.data)
                p = p.next
            else:
                s.append(q.data)
                q = q.next

        while p:
            s.append(p.data)
            p = p.next


        while q:
            s.append(q.data)
            q = q.next

        return s 



    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        if prev:
            self.head = prev

    def recursive_reverse(self):
        prev = None
        curr = self.head

        def recurseive_helper( prev, curr):
            if curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                recurseive_helper(prev, curr)
            else:
                self.head = prev
                return    

        recurseive_helper(prev, curr)

