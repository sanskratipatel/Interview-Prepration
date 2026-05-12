def move_zeros_to_end_brute(arr) :
    res = [] 
    for i in range(0 , len(arr)) : 
        if arr[i] != 0 : 
            res.append(arr[i]) 

    for i in range(len(res) , len(arr)) : 
        res.append(0) 
    return res 

def moves_zeros_to_end_optimal(arr) : 

    i=0
    if len(arr) >1 :
        while i < len(arr) : 
            if arr[i] == 0 : 
                break 
            i = i +1 

    if i == len(arr)  :
        return arr 
    j =i +1 
    while j < len(arr) : 
        if arr[j] != 0 : 
            arr[i], arr[j] = arr[j], arr[i] 
            i = i+1 
        j = j+1 
        
    return arr
        
