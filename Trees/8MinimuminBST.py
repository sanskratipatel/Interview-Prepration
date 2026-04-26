def minimum_in_bst(node) : 
    temp = node 
    while temp is not None :
        if temp.left is not None :
            temp = temp.left  

    return temp.val