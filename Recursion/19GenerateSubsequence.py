def func(index , subset , nums ,ans) :
    if index >= len(nums) : 
        ans.append(subset.copy()) 
        return 
    subset.append(nums[index])
    func(index=index+1 , subset=subset, nums=nums,ans= ans)  
    subset.pop() 
    func(index=index+1 , subset=subset, nums=nums,ans= ans)   
    return ans

nums = [1,23,3] 
ans = [] 
index =0 
subset = [] 
print(func(index , subset, nums ,ans) )

