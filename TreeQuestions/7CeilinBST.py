def ceil_in_bst(node , key) :  
    temp = node 
    ceil = -1 
    while temp is not None : 
        if temp.val == key : 
            return key 
        elif temp.val < key : 
            temp = temp.right 
        else : 
            ceil = temp.val 
            temp = temp.left 
            