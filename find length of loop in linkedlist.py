def len_of_loop(head):
    slow=head
    fast=head
    count=0
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=slow.next
            count+=1
            while slow!=fast:
                slow=slow.next
                count+=1
            return count
    return 0
print(len_of_loop())        
            
        
        
    