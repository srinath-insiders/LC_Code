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
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("Prev node does not exist")
            return

        newNode = Node(data)
        temp = prev_node.next
        prev_node.next = newNode
        newNode.next = temp

    def deletion_by_value(self, data):

        if self.head and self.head.data == data:
            temp = self.head.next
            self.head = temp
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        if curr is not None:
            prev.next = curr.next
            curr = None
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        
    def deletion_by_position(self, pos):
        
        if self.head:
            curr = self.head
            if pos == 0:
                self.head = curr.next
                curr = None
                return

            count = 1
            prev = curr
            curr = curr.next

            while curr and pos != count:
                prev = curr
                curr = curr.next
                count += 1

            if curr is not None:
                prev.next = curr.next
                curr = None

    def length(self):
        curr = self.head

        count = 0

        while curr:
            count +=1
            curr = curr.next

        return count    

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)    

    def nodeSwap(self, data_1, data_2):
        if data_1 == data_2:
            return

        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != data_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != data_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if curr_1 is None or curr_2 is None:
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

    def reverse_recursive(self, cur, prev):
        if not cur:
            self.head = prev
            return

        nxt = cur.next
        cur.next = prev
        prev = cur 
        cur = nxt 
        return self.reverse_recursive(cur, prev)

    def reverse_iterative(self):
    
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        self.head = prev

    def merge_two_sorted_llist(self, list):
        p = self.head
        q = list.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p

        return s                

    def move_tail_to_head(self):
            
        if self.head and self.head.next:

            prev = None
            tail = self.head

            while tail.next:
                prev = tail
                tail = tail.next

            prev.next = None
            tail.next = self.head
            self.head = tail

        pass


    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        result = LinkedList()
        add_on = 0
        sum = 0
        while p or q:
            if p:
                sum = sum + p.data
                p = p.next
            if q:
                sum = sum + q.data
                q = q.next

            if add_on == 1:
                sum += add_on

            result.append(sum % 10)

            if sum // 10 != 0:
                add_on = 1
            else:
                add_on = 0
            sum = 0    

        return result


llist = LinkedList()

llist.append(3)
llist.append(4)
llist.append(6)
llist.append(5)
llist.prepend(1)
llist.insert_after_node(llist.head, 2)
llist.deletion_by_value(3)
llist.deletion_by_position(2)
print("count - " + str(llist.length()))
print("recursive count - " + str(llist.length_recursive(llist.head)))
llist.nodeSwap(5,6)
llist.reverse_recursive(llist.head, None)
llist.reverse_iterative()

llist2 = LinkedList()
llist2.append(4)
llist2.append(7)

print("Print merge two sorted list")
llist.merge_two_sorted_llist(llist2)
llist.print_list()

print("Move tail to head")
llist.move_tail_to_head()
llist.print_list()

print("The above is list 1")

print("This is list 2")
llist2.print_list()
print("Add list one and list two")
llist.sum_two_lists(llist2).print_list()