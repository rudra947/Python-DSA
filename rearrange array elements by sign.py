arr=[5,10,-3,-1,-10,6]
def arrangeby_posneg(arr):
    n=len(arr)
    result=[0]*n
    pos_index,neg_index=0,1
    for i in range(0,n):
            if arr[i]>=0:
                result[pos_index]=arr[i]
                pos_index+=2
            else:
                result[neg_index]=arr[i]
                neg_index+=2
    return result
print(arrangeby_posneg(arr)) 
                       
                  
    