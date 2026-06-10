def height_of_tree(node ,count) : 
    if node  == None : 
        return 
    
    left =height_of_tree(node.left,count) 
    right = height_of_tree(node.right , count)  
    return 1 + max(left,right)

