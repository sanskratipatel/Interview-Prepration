def _missign_number(arr) : 
    sum = 0 
    total_sum =0 

    for i in range(0 , len(arr)+1)  :
        total_sum = total_sum + i 
        if i < len(arr)  :
            sum = sum+arr[i] 
    ans = total_sum -sum