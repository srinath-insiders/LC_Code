# Insert from the back
# Remove from the front

class Queue:
    def __init__(self):
        self.my_queue = []

    def is_empty(self):
        return [] == self.my_queue

    def get_queue(self):
        return self.my_queue

    def front(self):
        if not self.is_empty():
            return self.my_queue[0]

    def back(self):
        if not self.is_empty():
            return self.my_queue[-1]

    def size(self):
        return len(self.my_queue)

    def enqueue(self, val):
        self.my_queue.append(val) 

    def dequeue(self):
        if self.front():
            result = self.front()
            self.my_queue.remove(result)               
            return result

# queue = Queue()
# queue.enqueue("A")
# queue.enqueue("B")
# queue.enqueue("C")

# print(queue.get_queue())
# print(queue.dequeue())
# print(queue.get_queue())


