class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node    
    
    def reverse_linkedlist(self):
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev
    
    def display(self):
     temp = self.head

     while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")    
s1=Linkedlist()
s1.append(10)
s1.append(20)
s1.append(30)
s1.reverse_linkedlist()
print(s1.display())            
            