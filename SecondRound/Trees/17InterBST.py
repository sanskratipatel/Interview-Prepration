def insert_into_bst(node,target) : 
    temp = node 
    if node is not None :
        while True : 
            if temp.val > target :
                if temp.left is None : 
                    temp.left = Node(target) 
                    break
                temp = temp.left 
            else : 
                if temp.right is None :
                    temp.right = Node(target) 
                    break 
                temp = temp.right
    else : 
        node = Node(target)
        
    return node
