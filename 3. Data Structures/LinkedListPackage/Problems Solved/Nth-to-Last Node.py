from LinkedList import LinkedList

def nth_to_the_last_node(list, n):
    length = list.length()
    if n <= length:
        n = length - n
        count = 0
        cur = list.head
        while cur:
            if count == n:
                return cur.data
            count += 1
            cur = cur.next
    return

def nth_to_the_last_node_2(list, n):
    p = list.head
    q = list.head

    count = 1
    
    while p:
        if count >= n:
            break
        count += 1
        p = p.next

    while p.next and q:
        p = p.next
        q = q.next

    return q.data



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(nth_to_the_last_node(llist,4))
print(nth_to_the_last_node_2(llist,4))
