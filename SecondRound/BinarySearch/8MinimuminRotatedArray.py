def minimum_sroted_array(arr, key) : 
    low = 0 
    high = len(arr) -1 
    n=len(arr)-1 
    while low <= high : 
        mid = low + (high - low) //2 
        small_index = -1
        if mid != 0 : 
            prev = mid-1 
        else : 
            prev = n
        if mid != n : 
            next_ele = mid +1 
        else : 
            next_ele = 0 
        
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next_ele] : 
            small_index = mid 
            break 
        elif arr[low] <= arr[mid] :
            low = mid +1 
        else : 
            high = mid -1  
    return small_index