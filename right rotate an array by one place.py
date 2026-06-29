arr=[12,3,4,5,6,7,8,9,10]
def right_rotate(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr
print(right_rotate(arr))
#or only for python
def right_rotate(arr):
    arr[:]=arr[len(arr)-1]+arr[1:len(arr)-1]
    return arr
print(right_rotate(arr))    
    