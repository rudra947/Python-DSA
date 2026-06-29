def second_largest(arr):
    largest=arr[0]
    second_largest=arr[0]
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
    return second_largest
arr=[1,2,3,4,5,99]
print(second_largest(arr))