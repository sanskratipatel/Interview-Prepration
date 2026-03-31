nums = [74,52,4,63,2,-6,7,-34,4] 
smallest = float("inf") 
second_smallest = float("inf") 

for i in range(0 , len(nums)) : 
    if smallest > nums[i] : 
        second_smallest = smallest
        smallest = nums[i]  
    elif second_smallest > nums[i] and nums[i] < smallest : 
        second_smallest = nums[i]

print(smallest , second_smallest) 
    