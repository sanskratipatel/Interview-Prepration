def preorder_sequence(node) :
    if node is None: 
        return  
    print(node.val)
    preorder_sequence(node.left) 
    preorder_sequence(node.right) 


def post_order(node) : 
    if node is None: 
        return 
    
    post_order(node.left) 
    post_order(node.right) 
    print(node.val) 


def in_order(node) : 
    if node is None : 
        return 
    in_order(node.left) 
    print(node.val) 
    in_order(node.right)