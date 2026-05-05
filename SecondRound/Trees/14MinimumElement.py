def minimum_element_bst(node) : 
    while node is not None and node.left is not None: 
        node = node.left
        
    return node.val