def height_of_tree(node) : 
    if node is None:
        return 0
    
    left = height_of_tree(node.left )
    right = height_of_tree(node.right )
    return 1 + max(left,right)

