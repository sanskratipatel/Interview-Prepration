def combination_sums(arr ,target ) : 
    ans = [] 
    def solve(i ,combination,target) :
        if target== 0 : 
            ans.append(combination.copy())  
        if i == len(arr) or target < 0 : 
            return
        combination.append(arr[i])
        solve( i,combination ,target-arr[i])  
        combination.pop() 
        solve( i+1,combination ,target) 
    solve(0 , [], target) 
    return ans 

print(combination_sums([2,3,6,7], 7))

