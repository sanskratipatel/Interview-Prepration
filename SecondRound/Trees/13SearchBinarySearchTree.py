def search_binary_search_tree(node,target): 
    if node is None :
        return 
    if node.val == target : 
        return node 
    
    if node.val > target :  
        search_binary_search_tree(node.left,target) 
    else: 
        search_binary_search_tree(node.right, target)

    