def subsets_unique(arr, ans, i, res):
    if len(arr) == i :  
        res.add(tuple(ans))  
        return
    ans.append(arr[i])
    subsets_unique(arr , ans,i+1, res) 
    ans.pop()
    subsets_unique(arr , ans,i+1, res) 
       

arr = [1, 2, 2]
arr.sort() 
res = set()
subsets_unique(arr, [], 0 ,res) 

print(res)