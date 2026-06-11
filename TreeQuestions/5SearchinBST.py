temp = node 
while noe is not None : 
    if temp.val ==value : 
        return node.val 
    elif  value < temp.val :  
        temp = temp.left 
    else : 
        temp = temp.right  
return None 