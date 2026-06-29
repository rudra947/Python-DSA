
def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    return result+left[i:]+right[j:]

arr=[3,1,2,6,4,7,8,9,5,11]
def divide_array(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left=divide_array(left_half)
    right=divide_array(right_half)
    return merge_array(left,right)
print(divide_array(arr))    

                
    