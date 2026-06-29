class Solution:
    def func(self, num):
        if num==0 or num==1:
            return num
        return self.func(num-1)+self.func(num-2)

num=int(input("enter the number:"))    
s=Solution() 
print(s.func(num))   
    