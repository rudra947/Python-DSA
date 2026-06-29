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
    
    def middle_linkedlist(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow.data
s1=Linkedlist()             
s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
print(s1.middle_linkedlist())