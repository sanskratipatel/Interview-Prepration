def print_all_subsets(arr ,ans ,i ,res) : 
    if len(arr) == i : 
        res.append(ans.copy()) 
        return 
    ans.append(arr[i]) 
    print_all_subsets(arr, ans , i+1 ,res) 
    ans.pop()
    print_all_subsets(arr, ans , i+1)  

arr = [1, 2, 3]
res =[]
print_all_subsets(arr, [], 0 , res)  
print(res)