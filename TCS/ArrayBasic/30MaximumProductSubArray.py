arr = [2,3,-2,-3,4]  
product = 1 
suffix = 1 
ans =1
prefix =1 
j = len(arr)-1
for i in range(0 , len(arr)) : 
    if suffix == 0 : 
        suffix =1 
    if prefix == 0 : 
       prefix = 1  
    prefix = prefix * arr[i]
    suffix = suffix * arr[j]  
    product = max(prefix,suffix) 
    ans = max(product ,ans) 
    j = j-1
    

    