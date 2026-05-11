nums = [3,3,1,3,2,5] 
seen = set() 

for i in range(0 , len(nums)) :
    if nums[i] in seen : 
       print( nums[i]) 
       break 
    seen.add(nums[i])


slow = nums[0]
fast = nums[0] 

for i in range(0 , len(nums)) : 
    slow = nums[slow] +1
    fast = nums[nums[fast]] +1 
    if slow == fast : 
        print(slow)
        break