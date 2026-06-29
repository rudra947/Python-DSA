arr=[-2,1,-3,4,-1,2,1,-5,4]
def max_subarray(arr):
    maxi=arr[0]
    current=0
    for i in arr:
        current=current+i
        maxi=max(maxi,current)
        if current<0:
            current=0
            
    return maxi

print(max_subarray(arr))    
            