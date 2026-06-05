
def solve(index ,subset, nums ,count, target,total) : 
    if target == total :
        return 1
    if len(nums)<= index: 
        return 0
    if total > target :
        return 0
    subset.append(nums[index] )
    total = total + nums[index]
    pick = solve(index+1,subset, nums ,count, target,total )  
   
    subset.pop() 
    total = total - nums[index]
    not_pick = solve(index+1,subset, nums ,count, target,total )   
  
    return pick + not_pick
    


nums = [4,5,9]
ans = []
subset = []
print(solve(0 , subset, nums ,0 ,9 ,0) )
