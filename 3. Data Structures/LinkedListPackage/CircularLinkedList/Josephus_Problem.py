class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def remove_node(self, node):
        if self.head.next == self.head and self.head.data == node.data:
            self.head = None
            return

        prev = None
        curr = self.head
        
        while curr:
            if curr.data == node.data:
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
           
    def josephus(self, step):
        curr = self.head

        while curr.next != curr:
            count = 1
            while count != step:
                count += 1
                curr = curr.next
            next = curr.next
            print("Kill - "+str(curr.data))
            self.remove_node(curr)
            curr = next

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

Cll = CircularLinkedList() 


Cll.append(5)
Cll.append(6)
Cll.append(7)
Cll.append(8)

Cll.josephus(2)
Cll.printList()

