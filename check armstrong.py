n=int(input("input the number:"))
num=n
result=0
while num>0:
    ld=num%10
    result+=ld**len(str(n))
    num//=10
if result==n:
    print(f"{n}is armstrong")  
else:
    print(f"{n}is not armstrong")      