def predecessor_successor(node, key) : 
    if node is None : 
        return None 
    left = predecessor_successor(node.left, key) 
    if node.val > key : 
        return node.val 
    right = predecessor_successor(node.right, key) 
    
    
    