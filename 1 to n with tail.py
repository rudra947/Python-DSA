def func(i,n):
    if i>n:
        return
    func(i,n-1)
    print(n)
i=int(input("enter the number:"))    
n=int(input("enter final operaions:"))
func(i,n)
