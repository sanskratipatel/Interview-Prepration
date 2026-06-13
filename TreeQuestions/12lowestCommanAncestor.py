def lowest_comman_ancestor(node , p , q): 
    if node is None : 
        return None 
    if node == p or  node ==q :
        return node 
    
    left = lowest_comman_ancestor(node.left ,p ,q) 
    right = lowest_comman_ancestor(node.right , p , q) 
    if right == None and left == None : 
        return None 
    elif right == None: 
        return left
    elif left == None: 
        return right 

    return node  


 