
def solve(index ,subset, nums ,ans, target,total) : 
    if target == total : 
        ans.append(subset.copy()) 
        return True
    if len(nums)<= index: 
        return False
    if total > target :
        return False
    
    subset.append(nums[index] )
    total = total + nums[index]
    pick = solve(index+1,subset, nums ,ans, target,total )  
    if pick == True : 
        return True
    subset.pop() 
    total = total - nums[index]
    not_pick = solve(index+1,subset, nums ,ans, target,total )   
    
    return not_pick
    


nums = [4,5,9,3,1,5,2,6,2]
ans = []
subset = []
print(solve(0 , subset, nums ,ans ,9 ,0) )
