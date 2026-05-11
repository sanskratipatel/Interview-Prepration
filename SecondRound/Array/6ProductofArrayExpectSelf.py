def product_of_array_expect_self(arr) : 
    ans = [] 
    for i in range(0 , len(arr)) : 
        product = 1
        for j in range(0 , len(arr)) : 
            if i != j: 
                product = product * arr[j] 
        
        ans.append(product) 
    return ans 

def product_of_array_expect_self(arr) :   
    n = len(arr)
    prefix = [1] * n
    sufix = [1] * n
    ans = [1] * n
    ans =[]
    for i in range(1 , len(arr)) : 
        prefix[i] = prefix[i-1] * arr[i-1]  

    for j in range(len(arr)-2 , -1 , -1) :   
        sufix[i] = sufix[i+1] * arr[i+1]
    
    for k  in range(0 , len(arr)) : 
        ans[k] = sufix[k] * prefix[k]
