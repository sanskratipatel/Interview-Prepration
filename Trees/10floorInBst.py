def floor_in_bst(node ,floor) :
    ans = -1 
    temp = node 
    while temp is not None : 
        if temp.val == floor :
            return temp.val 
        elif temp.val > floor : 
            temp = temp.left  
        else :  
            ans = temp.val 
            temp = temp.right
