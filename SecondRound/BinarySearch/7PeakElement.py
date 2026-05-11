def peak_lement(arr, key) : 
    low = 0 
    high = len(arr) -1 
    n=len(arr)-1 
    while low <= high : 
        mid = low + (high - low) //2 
        peak_index = -1
        if mid != 0 : 
            prev = mid-1 
        else : 
            prev = n
        if mid != n : 
            next_ele = mid +1 
        else : 
            next_ele = 0 
        
        if arr[mid] >= arr[prev] and arr[mid] >= arr[next_ele] : 
            peak_index = mid 
            break 
        elif arr[prev] <= arr[mid] :
            low = mid +1 
        else : 
            high = mid -1 
  
    return peak_index


def peak_element(arr):

    low = 0
    high = len(arr) - 1
    n = len(arr)

    while low <= high:

        mid = low + (high - low) // 2

        # check left
        left = float("-inf") if mid == 0 else arr[mid - 1]

        # check right
        right = float("-inf") if mid == n - 1 else arr[mid + 1]

        # peak found
        if arr[mid] >= left and arr[mid] >= right:
            return mid

        # move right
        elif arr[mid] < right:
            low = mid + 1

        # move left
        else:
            high = mid - 1

    return -1