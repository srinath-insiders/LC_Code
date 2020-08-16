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
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = newNode
            return
    
    def printList(self):
        currNode = self.head

        while currNode:
            print(currNode.data)
            currNode = currNode.next

    def prepend(self, data):
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertAfterNode(self, prev_node, data):
        if not prev_node:
            print("prev node does not exist")
            return
        newNode = Node(data)

        newNode.next = prev_node.next
        prev_node.next = newNode

    def deleteByValue(self, data):
        if self.head:
            if self.head.data == data:
                node = self.head.next
                self.head = None
                self.head = node
            else:
                currNode = self.head
                while currNode.next:
                    if currNode.data == data:
                        break
                    else:
                        prevNode = currNode
                        currNode = currNode.next
                if currNode is not None:
                    prevNode.next =  currNode.next        
                    currNode = None
                    return
    
    def deleteByPosition(self, pos):
        currNode = self.head
        if pos == 0 and currNode:
            self.head = currNode.next
            currNode = None
        else:
            count = 1
            prevNode = currNode
            currNode = currNode.next
            while currNode:
                if count == pos:
                    prevNode.next = currNode.next
                    currNode = None
                    break
                else:
                    prevNode = currNode
                    currNode = currNode.next    
                    count += 1    
        return

    def lengthOfTheLinkedList(self):
        currNode = self.head
        count = 0
        while currNode:
            count += 1
            currNode = currNode.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append("1")
llist.append("2")
llist.append("3")
llist.prepend("4")
llist.insertAfterNode(llist.head.next.next,"9")
llist.deleteByValue("4")
llist.deleteByPosition(4)
llist.printList()
print('Iterative Func Length - '+str(llist.lengthOfTheLinkedList()))
print('Recursive Func Length - '+str(llist.len_recursive(llist.head)))
















