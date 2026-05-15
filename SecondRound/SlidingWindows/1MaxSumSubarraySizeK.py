def max_subarray_size_k(arr, k) : 
    sum = 0 
    i = 0 
    j = 0 
    ans = 0
    while j<len(arr) :
        sum = sum + arr[j] 
        if j-i+1 <k : 
            j=j+1 
        elif j-i+1 == k :  
            ans = max(ans, j-i+1) 
            sum =sum-arr[i]
            i = i+1 
            j = j+1 
        

