arr=[1,1,1,2,3,4,4,7,9,9,9,10]
def remove_duplicates(arr):
    n=len(arr)
    freq_map={}
    for i in range(0,n):
        freq_map[arr[i]]=0
    j=0
    for k in freq_map:
        arr[j]=k
        j+=1
    return j
print(remove_duplicates(arr))