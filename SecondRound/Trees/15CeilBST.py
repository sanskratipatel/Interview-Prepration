def ceil_in_bst(node,temp) : 
    ans = -1 
    while node is not None : 
        if node.val ==temp : 
            return node.val 
        if node.val > temp : 
            ans = node.val 
            node = node.left 

        else : 
            node = node.right 
    return ans 
   
