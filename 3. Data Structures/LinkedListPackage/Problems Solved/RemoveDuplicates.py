from LinkedList import LinkedList

def removeDuplicates(list):
    check_list = []
    cur = list.head 

    prev = None
    while cur:
        if cur.data in check_list:
            prev.next = cur.next
            cur = None
        else:
            check_list.append(cur.data)
            prev = cur
        cur = prev.next
    return list



llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
print("Removed Duplicates")
removeDuplicates(llist).print_list()

