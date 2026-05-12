def binary_tree(arr, key) : 
    low = 0 
    high = len(arr) -1 
    n = len(arr)
    first = -1
    while low<= high : 
        mid = low - (high +low) //2
        if arr[mid] == key :
            first = mid
            high = mid -1 
            
        elif arr[mid] < key : 
            low = mid +1 
        else : 
            high = mid -1 
    return -1
