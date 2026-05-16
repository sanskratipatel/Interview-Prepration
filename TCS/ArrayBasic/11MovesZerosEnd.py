def moves_zeros_at_end(arr) : 
    i = 0 
    j = 0 
    while j <len(arr) : 
        if arr[j] != 0 : 
            arr[i] , arr[j] = arr[j] ,arr[i] 
            i = i+1 
        j = j+1 
    return arr 