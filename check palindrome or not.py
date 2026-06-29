n=int(input("input the number:"))
num=n
result=0
while num>0:
    ld=num%10
    result=result*10+ld
    num//=10
if n==result:
    print(f"{n}is a plaindrome")  
else:
    print(f"{n} is not a palindrome")      
  
    