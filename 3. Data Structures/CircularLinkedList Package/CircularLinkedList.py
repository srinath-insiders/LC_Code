class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
    def __init__(self):
      self.head = None 

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head                           

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            if cur.next == self.head:
                break
            cur = cur.next


    def remove_node(self, node):
        if self.head:
            if self.head == node:
                if self.head.next == self.head:
                    self.head = None
                else:
                    next = self.head.next

                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = next
                    self.head = next        
            else:
                prev = None
                curr = self.head

                while curr:
                    if curr == node:
                        prev.next = curr.next
                        return
                    if curr.next == self.head:
                        break
                    prev = curr
                    curr = curr.next
                    
    def split_llist(self):
        curr = self.head
        if self.head:

            count = 1

            while curr.next != self.head:
                count = count + 1
                curr = curr.next
            
            if count > 1:
                curr.next = None

                curr = self.head
                mid = count // 2
                iterate = 1

                while iterate < mid:
                    curr = curr.next
                    iterate += 1

                second = curr.next 
                curr.next = self.head

                split_list = CircularLinkedList()
                while second:
                    split_list.append(second.data)
                    second = second.next

                self.print_list()
                print("\n")
                split_list.print_list()



    def josephus_problem(self, step_size):
        curr = self.head

        if curr:
            while curr.next != curr:
                count = 1
                while count < step_size:
                    count += 1
                    curr = curr.next
                next = curr.next
                self.remove_node(curr)
                curr = next

        print(curr.data)

cllist = CircularLinkedList()
cllist.append("2")
cllist.append("3")
cllist.prepend("1")
cllist.append("4")
cllist.remove_node("0")

#cllist.split_llist()

cllist.josephus_problem(4)
