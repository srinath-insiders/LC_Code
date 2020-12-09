from Linked_list import LinkedList


def count_occurences_iterative(list, data):
    curr = list.head
    count = 0
    
    while curr:
        if curr.data == data:
            count += 1
        curr = curr.next

    print("no. of occurences - "+ str(count))

def count_occurences_recursive(list, data):

    def count_helper(node, data):
        if node:
            if node.data == data:
                return 1 + count_helper(node.next, data)
            else:
                return count_helper(node.next, data)
        return 0              

    print("no. of occurences - "+ str(count_helper(list.head, data)))



list = LinkedList()
list.append(1)
list.append(3)
list.append(1)
list.append(1)
list.append(1)
count_occurences_iterative(list, 1)
count_occurences_recursive(list, 1)

