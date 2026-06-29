arr=[7,8,1,2,3,4,5,6]
def binary_search(arr):
    mini=float("inf")
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=arr[high]:
            mini=min(mini,arr[mid])
            high=mid-1
        else:
            mini=min(mini,arr[low])
            low=mid+1
    return mini
print(binary_search(arr))                