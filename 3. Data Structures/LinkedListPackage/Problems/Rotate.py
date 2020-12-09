from Linked_list import LinkedList

def rotate(list, pivot):
    count = 0

    curr = list.head
    node = None
    prev = None
    
    while curr and count <= pivot:
        count += 1

        if count == pivot:
            node = curr

        prev = curr
        curr = curr.next

    if node and prev and node.next:
        print(node.data)
        print(prev.data)
        print(node.next.data)
        prev.next = list.head
        next = node.next 
        list.head = next
        node.next = None
       

def print_list(list):
    curr = list.head

    while curr:
        print(curr.data)
        curr = curr.next


list = LinkedList()
list.append(1)
list.append(3)
list.append(1)
list.append(1)
list.append(1)
rotate(list, 1)
print_list(list)