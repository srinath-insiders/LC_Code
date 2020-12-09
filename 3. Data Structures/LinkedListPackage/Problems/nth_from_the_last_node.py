from Linked_list import LinkedList

def print_nth_from_the_last_node(llist, n):
    curr = llist.head
    length = 0
    

    while curr:
        length += 1
        curr = curr.next

    if n > length:
        return 

    target = length - n

    curr = llist.head
    while target > 0:
        curr = curr.next
        target -= 1

    print(curr.data)


def print_nth_from_the_last_node_method_2(llist, n):
    p = llist.head

    count = 0

    while count != n:
        count += 1
        if not p:
            return
        p = p.next

    curr = llist.head

    while p and curr:
        p = p.next
        curr = curr.next


    print(curr.data)



llist = LinkedList()
llist.append(1)
llist.append(9)        
llist.append(1)
llist.append(3)
llist.append(4)
llist.append(4)

print_nth_from_the_last_node(llist, 7)
print_nth_from_the_last_node_method_2(llist, 6)


