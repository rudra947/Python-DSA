from math import sqrt
n=int(input("enter number "))
result_of_factors=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        result_of_factors.append(i)
        if n//i!=i:
          result_of_factors.append(n//i)             
result_of_factors.sort()
print(f"Number of factors for {n} is {len(result_of_factors)} and the factors are {result_of_factors}")        
        