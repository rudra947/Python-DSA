arr=[1,99,98,101,2,5,3,100,1,1]
def longest_cons(arr):
    arr.sort()
    c=0
    last_smaller=float("inf")
    longest=0 
    for i in range(0,len(arr)):
        num=arr[i]
        if num-1==last_smaller:
            c+=1
            last_smaller=num
        elif num!=last_smaller:
            c=1
            last_smaller=num
        longest=max(longest,c)   
    return longest     
print(longest_cons(arr))    

    