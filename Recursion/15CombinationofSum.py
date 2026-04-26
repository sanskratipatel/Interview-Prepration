def get_all_combination(arr=[] , idx = 0 ,ans=None, target=0 , result = None ,seen = None):  
    if ans is None:
        ans = [] 
    if result is None:
        result = [] 
    if seen is None:
        seen = set()
    if target == 0 :
        temp = tuple(ans) 
        if temp not in seen : 
            seen.add(temp) 
            result.append(ans.copy()) 
        return result 
    if idx == len(arr) or target <0 : 
        return result 
    
    ans.append(arr[idx]) 
    get_all_combination(arr,idx+1 , ans , target -arr[idx] , result) 
    ans.pop() 
    get_all_combination(arr,idx+1 , ans , target ,result)  
    return result 
print(get_all_combination([2,3,1,6] , target=7))


