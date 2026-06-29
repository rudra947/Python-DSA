def check_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>=arr[i+1]:
            return False
    return True 
             
arr=[1,2,3,5,99]  
print(check_sorted(arr))      
        