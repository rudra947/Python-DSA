arr=[1,0,3,4]
def find_missing(arr):
    n=len(arr)
    expected=n*(n+1)//2
    total=sum(arr)
    return expected-total            
        
print(find_missing(arr))    