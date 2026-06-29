arr=[2,4,6,7,9,11,18,19]
target=int(input("enter the target element:"))
def binary_search(arr,low,high):
    if low>high:return -1
    mid=(low+high)//2 
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,mid+1,high)
    else:
        return binary_search(arr,low,mid-1)
print(binary_search(arr,0,len(arr)-1))