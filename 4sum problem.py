arr=[1,0,-1,0,-2,-2]
def foursum(arr):
    arr.sort()
    n=len(arr)
    result=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            
            while left<right:
             total=arr[i]+arr[j]+arr[left]+arr[right]
             if total< 0:
                left+=1
             elif total>0:
                right-=1
             else:
                result.append([arr[i],arr[j],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:
                    left+=1
    return result                      
print(foursum(arr))        