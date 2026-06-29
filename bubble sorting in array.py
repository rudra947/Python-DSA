arr=[4,99,11,8,1,8,3,5,9]
def bubble_sort(arr):
    n=len(arr)
    is_swap=False
    c=0
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                c+=1
                is_swap=True
    if is_swap==False:
        print("array is already sorted")
    print("sorted array is:",arr)                
    print("number of swaps:",c)                      

bubble_sort(arr)                   
                
        