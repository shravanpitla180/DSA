'''
-->Stack - Last In First Out(LIFO).

-> The elemnts inserted  in the last will be removed first.
-> Insertion and Deletion happens at the same end,called TOP.

--> Operation:-

-> Push(x) - Insert on element "x".
-> Pop(x) - Reemove the top element.
-> Peeks()/Top() - Represent top elements in stack.
-> isEmpty() - Check whether Stack is Empty or not.
-> Size() - Returns the no.of elements in Stack.

'''

class Stack:
    def __init__(self):
        self.stack = []
    # Inser an eelement
    def push(self,value):
        self.stack.append(value)
    # Delete an elements
    def pop(self):
        return self.stack.pop()
    # Return on top element
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    # check stack is empty or not
    def is_empty(self):
        return len(self.stack)==0
    # length or stack
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top: ",s.peek())
print("removed: ",s.pop())
s.display()
print("Size: ",s.size())
