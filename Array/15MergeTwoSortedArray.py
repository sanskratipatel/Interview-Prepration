arr1 = [1,2,3,4,5,6] 
arr2 = [1,2,3,4,5,6] 
ans = []
i = 0 
m = len(arr1) 
j =0 
n = len(arr2) 

while(i<m and j <n) : 
    if arr1[i] <= arr2[j] :  
        if len(ans) == 0 or ans[-1] != arr1[i] :
            ans.append(arr1[i]) 
        i = i+1 
    else: 
        if len(ans) == 0 or ans[-1] != arr2[j] :
            ans.append(arr2[j]) 
        j = j +1 

if i <m : 
     while(i <m) : 
        if len(ans) == 0 or ans[-1] != arr1[i] :
            ans.append(arr1[i])  
        i = i+1 

if j < n : 
    while(j< n) : 
        if len(ans) == 0 or ans[-1] != arr2[j] :
             ans.append(arr2[j])
        j = j +1 
    
print(ans)
    