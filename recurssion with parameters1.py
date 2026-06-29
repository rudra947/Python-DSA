def func(i,n):
    if i==n:
        print(i)
        return 
    print(i)
    func(i+1,n)

i=int(input("enter the number:"))
n=int(input("enter final operaions:"))
func(i,n)    