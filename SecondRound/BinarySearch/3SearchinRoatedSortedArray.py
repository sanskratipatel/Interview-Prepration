def search_roated_sorted_array(arr, key) : 
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
  
    l1= small_index
    h1 = len(arr) -1
    while l1<= h1 :
        m1 = l1 + (h1 - l1)//2 
        if arr[m1] == key : 
            return m1 
        elif arr[m1] < key : 
            l1 = m1+1 
        else : 
            h1 = m1 -1 

    l2= 0
    h2 = small_index-1
    while l2<= h2 :
        m2 = l2 + (h2 - l2)//2 
        if arr[m2] == key : 
            return m2 
        elif arr[m2] < key : 
            l2 = m2+1 
        else : 
            h2 = m2 -1 
    return -1