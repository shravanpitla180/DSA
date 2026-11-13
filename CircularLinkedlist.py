class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        #LL empty
        if self.head is None:
            new_node.next=new_node
            self.head=new_node
        #LL is not empty
        current=self.head
        while current.next != self.head:
            current=current.next
        new_node.next=self.head
        self.head=new_node

    def insert_at_ending(self,data):
        new_node=Node(data)
        #LL empty
        if self.head is None:
            new_node.next=new_node
            self.head=new_node
        #LL is not empty
        current=self.head
        while current.next != self.head:
            current=current.next
        new_node.next=self.head
        current.next=new_node

    def insert_at_position(self,position,data):
        if position<0:
            print("Invalid position")
            return
        new_node=Node(data)
        if position==0:
            new_node.next=new_node
            self.head=new_node
            return
        current=self.head
        for _ in range(position-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node

    def delete_at_beginning(self):
        #LL is empty
        if self.head is None:
            print("List is empty")
        #LL has one element
        if self.head.next==self.head:
            self.head=None
            return
        #LL has more than one element
        current=self.head
        while current.next!=self.head:
            current=current.next
        self.head=self.head.next
        current.next=self.head

    def delete_at_ending(self):
        #LL is empty
        if self.head is None:
            print("List is empty")
        #LL has one element
        if self.head.next == self.head:
            self.head=None
            return
        #LL has more than one element
        current=self.head
        while current.next.next != self.head:
            current=current.next
        current.next=self.head

    def length(self):
        if self.head is None:
            return 0 
        count=0
        current=self.head
        while True:
            count+=1
            current=current.next
            if current == self.head:
                break
        return count

    def display(self):
        current=self.head
        while True:
            print(current.data,end="->")
            current=current.next
            if current==self.head:
                break
        print("back to head")

cli=CircularLinkedList()
cli.insert_at_beginning(5)
cli.insert_at_ending(10)
cli.insert_at_ending(15)
cli.insert_at_position(3,20)
cli.display()
print(cli.length())
cli.delete_at_beginning()
cli.delete_at_ending()
cli.display()
