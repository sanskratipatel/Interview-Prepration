def two_sum(arr ,target) : 
    mydict = {} 

    for i in range(0 , len(arr)) :
        remianing = target -arr[i] 
        if remianing in mydict :
            return mydict[remianing] , arr[i]  
        else : 
            mydict[arr[i]] = i

        