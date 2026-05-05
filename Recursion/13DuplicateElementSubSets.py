def duplicate_element_subset(arr =[] , ans=[] ,i=0) : 
    if len(arr) == i : 
        print(ans) 
        return 
    ans.append(arr[i])
    duplicate_element_subset(arr, ans, i+1 )  
    ans.pop()
    idx = i+1 
    while(idx < len(arr) ) and arr[idx] == arr[idx-1] : 
        idx = idx +1 
    
    duplicate_element_subset(arr,ans, idx)
arr = [2,1,2] 
arr.sort() 
print(arr)  
duplicate_element_subset(arr, ans =[])