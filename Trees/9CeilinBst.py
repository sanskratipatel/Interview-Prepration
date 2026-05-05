def ceil_in_bst(node ,ceil) :
    temp = node 
    ans = -1
    while temp is not None :   
        if temp.val == ceil : 
            return temp.val 
        if temp.val < ceil : 
            temp = temp.right
        elif temp > ceil : 
            ans = temp.val
            temp = temp.left 
        



        