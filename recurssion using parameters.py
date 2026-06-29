def func(x,n):
    if n==0:
        return 
    print(x)
    func(x,n-1)
x=int(input("enter the number:"))
n=int(input("enter the number of times:"))    

func(x,n)