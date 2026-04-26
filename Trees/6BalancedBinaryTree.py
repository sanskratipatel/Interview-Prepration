# Balanced DiaMeter of binary tree 

# def height_balanced_tree(node) : 
#     if node is None : 
#         return   
#     lh = height_balanced_tree(node.left) 
#     if lh == -1 :
#         return -1
#     rh = height_balanced_tree(node.right)  
#     if rh == -1 :
#         return -1 
    
#     if abs(lh-rh) >1 :  
#         return -1 
#     return 1+ max(lh ,rh) 



# x = height_balanced_tree(node) 
# if x == -1 : 
#     print("Nottttttt") 
# else: 
#     print("Yesssssss")  



def balanced_tree_func(node):
    if node is None :
        return 
    lh = balanced_tree_func(node.left) 
    if lh == -1 : 
        return -1 
    rh = balanced_tree_func(node.right) 
    if rh == -1 :
        return -1 
    
    if abs(lh-rh) >1 :
        return -1 
    return 1 + max(lh+rh) 


x = balanced_tree_func(node) 
if x == -1 :
    print("noooo") 
else: 
    print("Yessss")