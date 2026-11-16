'''
Queue - First In First Out(FIFO).
=====

FIFO :- The element insertd fist will be removed first.
-->Insertion happens or rear
-->Deletion happens or front

Operations
===========
-->Enqueue(x) - Insert on element "x".
-->Dequeue() - Removes the first element.
-->Front() - Shows the first element.
-->Rear()- Shows last elemets.
--> Isempty() - Checks whether Queue is empty or not.
-->Size()- Returns no.of elements.

'''

class Queue:
    def __init__(self):
        self.queue = []
    # Insertion elemets
    def enqueue(self, value):
        return self.queue.append(value)
    # Deleting
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    # First elememnt
    def front(self):
        return self.queue[0] 
    def rear(self):
        return self.queue[-1]
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(10) 
q.enqueue(20)
q.enqueue(30)  
q.display()
q.dequeue()
q.display()
print("Front elememt: ",q.front())
print("rear element: ",q.rear())
print("IS Queue empty: ",q.is_empty())
print("Size of Queue: ",q.size())