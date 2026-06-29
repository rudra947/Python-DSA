nums=[5,6,7,7,1,9,11,1,1,5,1,1]
freq_map={}
x=int(input("Enter the number to find frequency:"))
for i in range(1,len(nums)):
    freq_map[nums[i]]=freq_map.get(nums[i],0)+1       
            
print(f"Frequency of {x} is {freq_map.get(x,0)} ")