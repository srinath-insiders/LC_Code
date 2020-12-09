from LinkedList import LinkedList

def count_occurences(list, data):
    count = 0
    cur = list.head
    
    while cur:
        if cur.data == data:
            count += 1
        cur = cur.next

    return count

def count_occurences_recursive(list, data):
    cur = list.head

    def count_recursive_helper(cur, data):
        if cur is None:
            return 0
        if cur.data == data:
            return 1 + count_recursive_helper(cur.next, data)
        else:
            return count_recursive_helper(cur.next, data)            

    return count_recursive_helper(cur, data)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("D")
llist.append("D")
llist.append("D")

print (count_occurences(llist, "D"))
print(count_occurences_recursive(llist, "D"))

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)

print (count_occurences(llist_2, 1))
print(count_occurences_recursive(llist_2, 1))