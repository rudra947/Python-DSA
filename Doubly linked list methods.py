class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_head(self,val):
        new_node=Node(val) 
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
    def append(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
    
    def insert_at_between(self,val,position):
        new_node=Node(val)
        if position==0:
            self.insert_at_head(val)
            return 
        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1
        if current is None:
            print("Position is out of bound")
            return 
        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node
    def display(self):
        print("node")
        curent=self.head
        while self.head is not None:
            print(current.data)
            current=current.next
s1=DoublyLinkedList()
s1.append(10)
s1.append(20)
s1.append(30)
s1.insert_at_between(40,1)                               
               