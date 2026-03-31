nums = [1,2,3,4,5,6,7,8,9,10] 

last = nums[len(nums)-1] 

for i in range(len(nums)-2, -1,-1):  
    nums[i+1] = nums[i]  

nums[0] = last
print(nums)