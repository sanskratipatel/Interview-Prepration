def longest_element(arr) : 
    small = arr[0] 

    for i in range(0 , len(arr)) :
        if small > arr[i] : 
            small = arr[i] 

    return small