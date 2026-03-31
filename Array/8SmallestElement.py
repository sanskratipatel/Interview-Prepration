nums = [12,42,54,64,77,3,52,4,-5] 
smallest = nums[0] 

for i in range(0 , len(nums)):
    if smallest > nums[i] : 
        smallest = nums[i] 

print(smallest)