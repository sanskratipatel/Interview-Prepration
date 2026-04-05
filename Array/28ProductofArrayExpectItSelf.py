arr = [1,2,3,4] 

ans = []

for i in range(0 , len(arr)) : 
    product = 1 
    
    for j in range(0 , len(arr)) : 
        if i != j : 
            product = product * arr[j] 
    ans.append(product) 

print(ans) 

res = [1] * len(arr)
prefix = [1] * len(arr)
suffix = [1] * len(arr)

for i in range( 1 , len(arr)): 
    prefix[i] = prefix[i-1] * arr[i-1] 

for j in range(len(arr)-2 , -1 , -1) : 
    suffix[j] = suffix[j+1] * arr[j+1]  

for i in range(0 , len(arr)) : 
    res[i] = prefix[i] * suffix[i] 
print(res)
