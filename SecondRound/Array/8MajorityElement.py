def majority_element(arr) : 
    my_dict = {} 
    for i in range(0 , len(arr)) : 
        if arr[i] not in my_dict : 
            my_dict[arr[i]] = 1 
        else : 
             my_dict[arr[i]]  =  my_dict[arr[i]] +1 
    n = len(arr) 
    n1 = n//2 
    for key in my_dict : 
        if my_dict[key] > n1:
             return key 
    
    return -1
            