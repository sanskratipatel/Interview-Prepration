def pre_order(node) : 
    if node == None : 
        return 
    print(node.val , end =" " ) 
    pre_order(node.left) 
    pre_order(node.right)  


def in_order(node) : 
    if node == None : 
        return 
    in_order(node.left) 
    print(node.val , end =" " ) 
    in_order(node.right,)  


def post_order(node) : 
    if node == None : 
        return 
    post_order(node.left) 
    post_order(node.right)  
    print(node.val , end =" " )  
