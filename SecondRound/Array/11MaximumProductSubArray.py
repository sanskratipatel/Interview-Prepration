def maximum_product_subArray(arr) : 
    maxproduct = arr[0]
    for i in range(0 , len(arr)) : 
        product = 1 
        for j in range(i , len(arr)) :  
            product = product * arr[j] 
            maxproduct = max(product , maxproduct) 
    return maxproduct


def maximum_product_subArray_optimal(arr) :
    prefix = 1
    sufix = 1
    n = len(arr)
    maxi = float("-inf")
    for i in range(0 , len(arr)):  
        if prefix == 0  : 
            prefix = 1 
        if sufix ==0 : 
            sufix = 1 

        prefix = prefix * arr[i] 
        sufix = sufix * arr[n-i-1] 
        maxi = max(maxi , max(sufix, prefix)) 
    return maxi




