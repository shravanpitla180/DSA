# Linkedlist
'''
A linked list is a data structure made of nodes. Each node stores a value and a link to the next node;
in a doubly linked list, it also links to the previous node.

-->Linear Data Structure
-->Data os stored in the form of nodes.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position cannot be negative")
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position is out of range")
            current = current.next
        if current is None:
            raise IndexError("Position is out of range")
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list")
        self.head = self.head.next

    def delete_at_ending(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position < 0:
            raise ValueError("Position cannot be negative")
        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list")
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position is out of range")
            current = current.next
        if current.next is None:
            raise IndexError("Position is out of range")
        current.next = current.next.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_ending(20)
ll.insert_at_position(2, 15)
ll.display()  # 5 --> 10 --> 15 --> 20 --> None
ll.delete_at_beginning()
ll.delete_at_position(1)
ll.delete_at_ending()
ll.display()  # 10 --> None
ll.insert_at_ending(20)
ll.insert_at_ending(30)
ll.display()  
print("Search for 20:", ll.search(20))
print("Length of ll:", ll.length())
ll.reverse()
ll.display() 
print("Has cycle:", ll.has_cycle())
