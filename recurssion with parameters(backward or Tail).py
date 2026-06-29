def func(i,n):
    if i>n:
        return 
    func(i+1,n)
    print(i)
i=int(input("enter the number:")) 
n=int(input("enter final operations:"))
func(i,n)   