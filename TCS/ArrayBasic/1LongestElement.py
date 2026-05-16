def longest_element(arr) : 
    largest = arr[0] 

    for i in range(0 , len(arr)) :
        if largest < arr[i] : 
            largest = arr[i] 

    return largest