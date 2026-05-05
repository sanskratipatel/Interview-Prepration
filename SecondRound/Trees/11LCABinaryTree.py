# Lowest common Ancestor Binary Tree 

def LCA(root, p ,q) :   
    if root is None : 
        return None 
    
    if root == p or root  == q : 
        return root 
    left_lca = LCA(root.left , p ,q) 
    right_lca = LCA(root.right , p , q) 
    if (left_lca and right_lca) : 
        return root 
    elif left_lca != None : 
        return left_lca 
    else :
        return right_lca
    



