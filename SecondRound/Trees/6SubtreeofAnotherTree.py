def tree_in_subtree(mainNode , subNode) :  
    if mainNode is None or subNode is None : 
        return mainNode == subNode
    if (mainNode.val == subNode.val and identical_tree(mainNode , subNode)): 
        return 
    return tree_in_subtree(mainNode.left , subNode.left) or tree_in_subtree(mainNode.right, mainNode.right) 

def identical_tree(node1, node2) : 
    if node1 is None or node2 is None : 
        return node1 == node2 
    
    isRightsame = identical_tree(node1.right , node2.right) 
    isLeftsame = identical_tree(node1.left, node1.left) 

    return isLeftsame and isRightsame and (node1.val == node2.val)