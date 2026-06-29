k=int(input("enter by how many palce to rotate:"))
arr=[1,2,3,4,5,6,7,8,9]
def rotate_right(arr):
    n=len(arr)
    k1=k%n
    arr[:]=arr[n-k1:]+arr[:n-k1]
    return arr

print(rotate_right(arr))
        