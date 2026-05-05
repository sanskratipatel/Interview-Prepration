def identical_tree(node1, node2) :
    if node1 is None or node2 is None:
        return node1 == node2 
    isLeftsame = identical_tree(node1.left , node2.left) 
    isRightsame = identical_tree(node1.right , node2.right)  

    return isLeftsame and isRightsame and (node1.val == node2.val)
