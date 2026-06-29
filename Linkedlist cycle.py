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
    
    def cycle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=self.head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
s1=Linkedlist()
s1.append(5)    
s1.append(9)
s1.append(1)
s1.append(7)
s1.append(6)
s1.append(1)
s1.append(9)
s1.append(2)
s1.append(8)
print(s1.cycle())              
            
                        