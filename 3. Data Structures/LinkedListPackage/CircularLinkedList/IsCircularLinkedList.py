

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

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next and curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            curr.next.next = self.head

    def prepend(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            curr = self.head

            while curr.next and curr.next != self.head:
                curr = curr.next

            curr.next = newNode
            newNode.next = self.head
            self.head = newNode                   

    def remove_node(self, data):
        if self.head.next == self.head and self.head.data == data:
            self.head = None
            return

        prev = None
        curr = self.head
        
        while curr:
            if curr.data == data:
                if prev:
                    next = curr.next
                    prev.next = next
                else:
                    current = self.head
                    while current.next and current.next != self.head:
                        current = current.next                            
                    next = self.head.next
                    current.next = next
                    self.head = next    
                break

            prev = curr
            curr = curr.next

            if curr == self.head:
                break

    def isCircularLinkedList(self, list):
        curr = list.head

        while curr:
            curr = curr.next

            if curr == None:
                return False

            if curr == list.head:
                return True    


    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

Cll = CircularLinkedList()

Cll.prepend(4)
Cll.append(5)

llist = LinkedList()
llist.append("A")

print(Cll.isCircularLinkedList(Cll))
print(Cll.isCircularLinkedList(llist))



