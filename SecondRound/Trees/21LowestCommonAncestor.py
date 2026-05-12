def lowest_common_ancestor(root ,p ,q):
    if root is None:
        return 
    if root == p or root ==q :
        return q 
    left = lowest_common_ancestor(root.left, p , q) 

    right = lowest_common_ancestor(root.right , p ,q) 

    if right and left :
        return root 
    elif left is not None:
        return root.left 
    else :
        return root.right