arr=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target=int(input("enter the target:"))
def binary_search(arr,low,high):
    n=len(arr)
    hb=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            hb=mid
            low=mid+1
        else:
            high=mid-1
    return hb
print(binary_search(arr,0,len(arr)))              