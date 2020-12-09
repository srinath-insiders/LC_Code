from LinkedList import LinkedList

def rotate_by_pivot_srinath(list, pivot):
    cur = list.head
    tail = None
    count = 0

    modify = False
    while cur:
        count += 1 
        if count == pivot:
            tail = cur.next
            modify = True
            cur.next = None
        if modify:
            if tail is None:
                return list
            cur = tail
            modify = False
        else:
            prev = cur
            cur = cur.next
        
    if count < pivot:
        return list
             
    prev.next = list.head
    list.head = tail     
    
    return list

def rotate_by_pivot_algo(list, pivot):
    p = list.head
    q = list.head

    count = 0
    
    while p.next:
        count += 1
        if count >= pivot:
            break
        p = p.next

    prev = None
    while p.next and q:
        p = p.next
        prev = q
        q = q.next

    if prev:
        p.next = list.head
        prev.next = None
        list.head = q

    return list  


llist_2 = LinkedList()
llist_2.append("1")
llist_2.append("2")
llist_2.append("3")
llist_2.append("4")
llist_2.append("5")
llist_2.append("6")

#rotate_by_pivot_srinath(llist_2,5).print_list()

rotate_by_pivot_algo(llist_2,3).print_list()