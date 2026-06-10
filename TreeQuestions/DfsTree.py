def pre_order_traversal_dfs(node) : 
    if node == None : 
        return 
    print(node.data , end= '' ) 
    pre_order_traversal_dfs(node.left) 
    pre_order_traversal_dfs(node.right) 



def in_order_traversal(node) : 
    if node == None : 
        return 
   
    in_order_traversal(node.left)  
    print(node.data , end= '' ) 
    in_order_traversal(node.right) 

def post_order_traversal(node) : 
    if node == None : 
        return 
    
    post_order_traversal(node.left) 
    pre_order_traversal_dfs(node.right) 
    print(node.data, end = " ") 
    