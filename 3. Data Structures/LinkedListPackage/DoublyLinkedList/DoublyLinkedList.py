class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = newNode
            newNode.prev = curr
        pass
       
    def prepend(self, data):
        newNode = Node(data)
        if self.head:
            head = self.head
            newNode.next = head
            head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode    
        pass

    def add_after_node(self,key, data):
        newNode =  Node(data)
        curr = self.head

        while curr:
            if curr.data == key and curr.next:
                next = curr.next
                curr.next = newNode
                newNode.next = next
                next.prev = newNode
                newNode.prev = curr
                pass
            elif curr.data == key and curr.next is None:
                curr.next = newNode
                newNode.prev = curr
                pass
            curr = curr.next        

    def add_before_node(self, key, data):
        newNode = Node(data)
        curr = self.head

        while curr:
            if curr.data == key and curr == self.head:
                newNode.next = curr
                curr.prev = newNode
                self.head = newNode
                break
            elif curr.data == key and curr != self.head:
                prev = curr.prev
                newNode.next = curr
                prev.next = newNode
                curr.prev = newNode
                newNode.prev = prev
                break
            curr = curr.next

    def delete_node(self, key):
        curr = self.head

        if curr.data == key and curr.next is None:
            curr = None
            self.head = None
            return

        if curr.data == key and curr.next:
            next = curr.next
            next.prev = None
            curr.next = None
            curr = None
            self.head = next
            return

        while curr:
            
            if curr.data == key and curr.next:
                next = curr.next
                prev = curr.prev
                prev.next = next
                next.prev = prev
                curr.next = None
                curr.prev = None
                curr = None
                break

            if curr.data == key and curr.next is None:
                prev = curr.prev
                curr.prev = None
                curr = None
                prev.next = None
                break
            
            curr = curr.next  

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            curr.prev = curr.next
            curr.next = prev
            prev = curr
            curr = curr.prev

        self.head = prev    

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        pass
        

DList = DoublyLinkedList()
DList.append(0)
DList.append(1)
DList.append(2)
DList.append(3)
DList.append(4)
DList.append(5)
DList.append(6)
DList.append(7)
DList.add_after_node(0, 111)
DList.add_after_node(2, 212)
DList.add_after_node(6, 999)
DList.add_after_node(7, 909)
DList.add_after_node(71, 10000)
DList.add_before_node(0, 52)
DList.add_before_node(111, 256)
DList.add_before_node(909, 77)
DList.delete_node(212)
DList.delete_node(77)
DList.delete_node(909)
DList.delete_node(0)
DList.printList()
print("\n")
DList.reverse()
DList.printList()
