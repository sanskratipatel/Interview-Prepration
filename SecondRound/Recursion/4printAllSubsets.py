def print_all_subsets(arr ,ans ,i) : 
    if len(arr) == i : 
        print(ans)  
        return
    ans.append(arr[i]) 
    print_all_subsets(arr, ans , i+1) 
    ans.pop()
    print_all_subsets(arr, ans , i+1)  

arr = [1, 2, 3]
print_all_subsets(arr, [], 0)