arr = [1,1,2,2,3,4,4,5]
i = 0 

for j in range(0 , len(arr)) : 
    if arr[i] != arr[j] : 
        i = i +1 
        arr[i] = arr[j]  
print(arr[:i+1]) 

ans = [] 
arr = [1,1,2,2,3,4,4,5]
for k in range(0 , len(arr)) : 
    if arr[k] not in ans : 
        ans.append(arr[k]) 
print(ans)
