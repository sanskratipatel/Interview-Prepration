nums = [1,2,3,4,5,6,7,8,9] 
k = 5
n = len(nums) 
rotation = k%n 

for i in range(0 , rotation) : 
    e = nums.pop() 
    nums.insert(0, e) 

print(nums)