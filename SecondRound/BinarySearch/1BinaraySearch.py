def binary_tree(arr, key) : 
    low = 0 
    high = len(arr) -1 
    n = len(arr)
    while low<= high : 
        mid = low - (high +low) //2
        if arr[mid] == key :
            return mid 
        elif arr[mid] < key : 
            low = mid +1 
        else : 
            high = mid -1 
    return -1

