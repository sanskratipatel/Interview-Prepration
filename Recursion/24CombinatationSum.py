def combinationSum(arr , target) : 
    ans = [] 
    index = 0 
    def solve(arr, ans ,index ,target , subset,sum) : 
       
        if target == sum : 
           
            ans.append(subset.copy()) 
            return 
        if len(arr) <= index : 
            return 
        if target < sum : 
            return
        sum = sum + arr[index]
        subset.append(arr[index])
        solve(arr, ans ,index  , target , subset ,sum) 
        sum = sum -arr[index]
        subset.pop()
        solve(arr, ans ,index +1  , target , subset ,sum)   
        return ans  
    
    solve(arr, ans ,0 ,target,[] ,0) 

    return ans 

arr =[2,3,6,7]

target =7 
print(combinationSum(arr,target))

    

        