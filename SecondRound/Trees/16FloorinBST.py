def floor_in_bst(node,temp) : 
    ans = -1 

    while node is not None :
        if node.val == temp : 
            return node.val 
        
        if node.val > temp : 
            node = node.left 
        else : 
            ans = node.val 
            node = node.right 

    return ans