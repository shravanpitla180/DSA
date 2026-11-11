class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    #Insert at beginning
    def insert_ata_beginning(self,data):
        new_Node = Node(data)
        # DLL is empty
        if self.head is Node:
            self.head = new_Node
            self.tail = new_Node
            return
        # DLL is not empty
        new_Node.next = self.head
        self.head.prev = new_Node
        self.head = new_Node

    def insert_at_ending(self, data):
        new_Node = Node(data)
        if self.head is Node:
            self.head = new_Node
            self.tail = new_Node
            return
        # DLL is not empty
        self.tail.next = new_Node
        new_Node.prev = self.tail
        self.tail = new_Node

    def insert_at_position(self,position,data):
        if position < 0 or position > self.length():
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return
        if position == self.length():
            self.insert_at_ending(data)
            return
        new_Node = Node(data)
        current = self.head
        for _ in range(position):
            current = current.next
        previous_Node = current.prev
        new_Node.prev = previous_Node
        new_Node.next = current
        previous_Node.next = new_Node
        current.prev = new_Node

    def delete_from_beginning(self):
        # DLL has one element
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_at_position(self,position):
        if position < 0 or position > self.length():
            print("Invalid position")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        if position == self.length():
            self.insert_at_ending()
            return
            current = self.head
        for _ in range(position):
            current = current.next
            