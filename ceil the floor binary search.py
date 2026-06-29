arr=[3,4,4,4,8,9,9,10,12,12,14,15]
target=int(input("enter the target:"))
def binary_search(arr):
        ceil=-1
        floor=-1
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return [arr[mid],arr[mid]]

            elif arr[mid]>target:
                ceil=arr[mid]
                high=mid-1
            else:
                floor=arr[mid]
                low=mid+1
        return [ceil,floor]                            
print(binary_search(arr))        