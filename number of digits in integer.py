from math import *
n=int(input("enter the number:"))
num=n
def count_digit(num):
    return int(log10(num)+1)
print(count_digit(num))