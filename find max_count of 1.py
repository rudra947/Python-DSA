arr=[1,1,0,1,1,1,0,1,1,1,1,0,1,1]
def max_occuring_of1(arr):
    c=0
    max_count=0
    for i in range(0,len(arr)):
        if arr[i]==1:
            c+=1    
        else:
            max_count=max(max_count,c)
            c=0
    return max_count

print(max_occuring_of1(arr))                
            
        