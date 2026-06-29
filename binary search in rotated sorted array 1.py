arr=[17,18,20,1,3,4,5,7,8,10,11,13,14,16]
def binary_search(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:return mid
        elif arr[mid]<=arr[high]:
            if arr[mid]<=target<=arr[high]:low=mid+1
            else:high=mid-1
        else:
            if arr[low]<=target<=arr[high]:high=mid-1
            else:low=mid+1
    return -1
target=int(input("enter the target element:"))
print(binary_search(arr,target))                