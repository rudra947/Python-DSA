arr=[1,2,3,3,3,3,3,5,6,8,9,9,10]
class Solution:
    def lower_bound(self,arr,target):
        low,high=0,len(arr)-1
        lb=-1
        while low<=high:
            mid=(low+high)//2 
            if arr[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def upper_bound(self,arr,target):                              
        low,high=0,len(arr)-1
        ub=-1
        while low<=high:
            mid=(low+high)//2 
            if arr[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
    def first_and_last(self,arr,target):
        if self.lower_bound(arr,target)==-1:
            return [-1,-1]
        else:
            return [self.lower_bound(arr,target),self.upper_bound(arr,target)-1]
s=Solution()
target=int(input("enter the target:"))
print(s.first_and_last(arr,target))        
                