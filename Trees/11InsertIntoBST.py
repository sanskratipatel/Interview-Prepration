def insert_into_bst(node , val) :
    temp = node 

    if node is None :
        return  Node(val) 
    while True : 
        if val < temp.val: 
            if temp.left is None:
                temp.left = Node(val )
                break
            temp = temp.left  
        elif val > temp.val : 
            if temp.right is not None:
                temp.right = Node(val) 
                break 
