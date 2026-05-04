def diameter_of_tree(node) : 
    if node is None :
        return 0 
    
    left = diameter_of_tree(node.left) 
    right = diameter_of_tree(node.right) 
    curr_dia = height(node.left) +  height(node.right) 
    return max(curr_dia , right ,left) 

def height(node) : 
    if node is None :
        return 0 
    lf = height(node.left) 
    rg = height(node.right) 
    return 1 + max(lf,rg) 

