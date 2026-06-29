class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SinglyLinkedList:
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
            
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current=self.head
            while current is not None:
                print(current.value,end=" ")
                current=current.next
            print()
    
    def insetat(self,value,pos):
        new_node=Node(value)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            count=0
            prev_node=None
            while current is not None and count<pos:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current
    
    def delete(self,value):
        temp=self.head
        if temp.next is not None:
            if temp.value==value:
                self.head=temp.next
                return 
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.value==value:
                        found=True
                        del temp
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    del temp
                    return
                else:print("node not found")
                
                 
s1=SinglyLinkedList()
s1.append(10)
s1.append(20)                
s1.traverse()
s1.delete(10)
s1.traverse()