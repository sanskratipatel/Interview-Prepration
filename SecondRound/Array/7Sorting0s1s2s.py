def sorting_colors(arr) : 
    count_zero = 0 
    count_one = 0 
    count_twos = 0  

    for i in range(0 , len(arr)) : 
        if arr[i] == 1 : 
            count_one = count_one +1 
        elif arr[i] == 0 : 
            count_zero = count_zero +1  
        else : 
            count_twos = count_twos +1 
    
    for i in range(0 ,count_zero) :  
        arr[i] = 0 
    n = count_one +count_zero
    for j in range(count_zero , n) :
        arr[j] = 1
   
    for k in range(n , count_twos) : 
        arr[k] = 2
    return arr


