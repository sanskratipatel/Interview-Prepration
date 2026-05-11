def search_insert_poistion(arr, key) : 
    low = 0 
    high = len(arr)-1 
    upper_bound = -1 
    while low<= high : 
        mid = low +(high-low)//2 
        if arr[mid] >= key:
            upper_bound = mid 
            high=mid - 1 
        elif arr[mid] < key : 
            low = mid+1
        else : 
            high = mid-1 
    return upper_bound