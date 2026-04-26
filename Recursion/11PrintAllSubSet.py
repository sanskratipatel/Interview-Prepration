def subsets(arr=[] , ans =[] , i=0) : 
    if i == len(arr): 
        
        print(ans) 
        return 
    ans.append(arr[i]) 
    subsets(arr,ans , i+1)  
    ans.pop() 
    subsets(arr,ans , i+1)  

arr=[1,2,3] 
ans = [] 
subsets(arr,ans)