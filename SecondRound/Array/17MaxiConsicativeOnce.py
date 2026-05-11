def maximum_one_consecative(arr) : 
    maxi = 0 
    count = 0
    for i in range(0 , len(arr)) : 

        if arr[i] ==1: 
            count = count +1 
        else : 
            count = 0 
        maxi = max(maxi,count) 
    return maxi
