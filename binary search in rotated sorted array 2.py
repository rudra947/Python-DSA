arr=[7,7,7,7,7,7,7,1,2,3,4,5,7,7]
def binary_search(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:return True
        elif arr[mid]==arr[high]==arr[low]:
            low+=1
            high-=1
            continue
        elif arr[mid]<=arr[high]:
            if arr[mid]<=target<=arr[high]:
                low=mid+1
            else:
                high=mid-1    
        else:
            if arr[low]<=target<=arr[high]:high=mid-1
            else:low=mid+1
    return False
target=int(input("enter the target element:"))
print(binary_search(arr,target))            