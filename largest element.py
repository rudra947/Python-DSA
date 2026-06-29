def largest(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest
arr=[1,2,3,4,5,99]
print(largest(arr))
    