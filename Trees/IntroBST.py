# Search in binary search tree 
def binary_search_tree(val , node):
    temp = node 
    while temp is not None : 
        if temp.val == val:  
            return temp
        elif temp.val > val : 
            temp = temp.left 
        else : 
            temp = temp.right