def insert_into_tree(node , key) : 
    if node is None : 
        return Node(key ) 
    temp = node
    while True: 
        if temp.val > key : 
            if temp.left is None : 
                temp.left = Node(key) 
                break 
            temp = temp.left 
        else : 
            if temp.right is None : 
                temp.right = Node(key) 
                break 
            temp = temp.right 
    return root
