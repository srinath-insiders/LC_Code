from Linked_list import LinkedList


def remove_duplicates(list):
    curr = llist.head
    list = dict()
    prev = None

    while curr:
        
        if curr.data in list:
            prev.next = curr.next
            curr = prev.next
        else:
            list[curr.data] = 1
            prev = curr
            curr = curr.next

    return llist    

llist = LinkedList()
llist.append(1)
llist.append(9)        
llist.append(1)
llist.append(3)
llist.append(4)
llist.append(4)

remove_duplicates(llist).print_list()




