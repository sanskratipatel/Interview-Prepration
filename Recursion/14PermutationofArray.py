def genrate_all_permutations(arr =[],idx =0, ans =[]): 
    if idx == len(arr) : 
        ans.append(arr.copy())  
        return ans

    for i in range(idx , len(arr)) :
        arr[idx] , arr[i] = arr[i] , arr[idx] 
        genrate_all_permutations(arr,idx+1 , ans)  
        arr[idx] , arr[i] = arr[i] , arr[idx]  
    return ans

arr= [1,2,3]
print(genrate_all_permutations(arr, 0 , ans = []))