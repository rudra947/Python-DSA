arr=[1,0,2,4,3,0,0,3,5,1]
def move_zeroestoend(arr):
    n=len(arr)
    temp=[]
    for i in arr:
        if i!=0:
            temp.append(i)
    for i in arr:
        if i==0:
            temp.append(i)
                        
    return temp

print(move_zeroestoend(arr))               
                    
                    
            