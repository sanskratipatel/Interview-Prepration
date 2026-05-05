def get_all_subset_in_array(arr=[] , ans = [] , i = 0,all_sub_set =None) : 
    if all_sub_set is None:
        all_sub_set = []
    if len(arr) == i : 
        all_sub_set.append(ans.copy()) 
        return all_sub_set
    ans.append(arr[i])
    get_all_subset_in_array(arr , ans , i+1,all_sub_set)  
    ans.pop() 
    get_all_subset_in_array(arr,ans, i+1,all_sub_set)  
    return all_sub_set


arr = [1,2,3,4] 
ans = [] 
print(get_all_subset_in_array(arr, ans))
