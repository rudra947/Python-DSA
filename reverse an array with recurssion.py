arr=[2,4,1,7,6,3,8,9,5]
def func(arr, left, right):
    if left >= right:
         return
    else:
        arr[left], arr[right] = arr[right], arr[left]
        func(arr, left + 1, right - 1)
func(arr, 0, len(arr) - 1)
print(arr)