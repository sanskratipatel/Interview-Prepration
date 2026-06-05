def combination_sum_result_with_unique(arr ,target) : 
    ans = [] 
    result = set()
    def solve(arr ,target , result, subset, total ,index) : 
        if target == total : 
            subset.sort()   
            result.add(tuple(subset)) 
            return 
        if target < total : 
            return 
        if len(arr) <= index :
            return 
        
        total = total + arr[index] 

        subset.append(arr[index]) 

        solve(arr,target, result, subset, total , index +1) 
        subset.pop() 
        total = total -arr[index]  
        solve(arr,target, result, subset, total , index +1) 
        return result 
    
    solve(arr,target, result,[] ,0 ,0) 
    return list(result) 

arr = [2,2,3,4,1] 
target =7

print(combination_sum_result_with_unique(arr, target))
            
        
0




















































































