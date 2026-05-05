def permutation_of_arr(nums) : 
    ans = [] 
    def solve(nums,ans ,i) : 
        if len(nums) == i : 
            ans.append(nums.copy()) 
            return

        for j in range(i , len(nums)) : 
            nums[i], nums[j] = nums[j] , nums[i] 
            solve(nums, ans ,i+1 ) 
            nums[i], nums[j] = nums[j] , nums[i]  

    solve(nums, ans ,0)  
    return ans
print(permutation_of_arr([1, 2, 3]))