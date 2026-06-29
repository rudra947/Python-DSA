arr=[5,9,1,2,4,15,6,3]
target=int(input("input target integer:"))
def two_sum(arr):
    n=len(arr)
    hash_map={}
    for i in range(0,n):
        remaining=target-arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[arr[i]]=i
            

print(two_sum(arr))            