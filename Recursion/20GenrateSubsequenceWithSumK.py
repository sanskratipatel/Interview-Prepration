def func(index,subset, nums,ans,target) : 
    if len(nums) <= index : 
        if sum(subset) == target:
           ans.append(subset.copy()) 
        return
    subset.append(nums[index]) 
    func(index+1 , subset, nums ,ans ,target) 
    subset.pop()
    func(index +1 , subset, nums ,ans ,target) 
    return ans
nums = [1,2,3 ,5,9 ,4,6] 
ans = [] 
index =0 
subset = [] 
print(func(index , subset, nums ,ans ,9) )


def solve(index ,subset, nums ,ans, target,total) : 
    if target == total : 
        ans.append(subset.copy()) 
        return
    if len(nums)<= index: 
        return
    if total > target :
        return 
    
    subset.append(nums[index] )
    total = total + nums[index]
    solve(index+1,subset, nums ,ans, target,total ) 
    subset.pop() 
    total = total - nums[index]
    solve(index+1,subset, nums ,ans, target,total )  

    return ans 
ans = []
subset = []
print(solve(0 , subset, nums ,ans ,9 ,0) )
