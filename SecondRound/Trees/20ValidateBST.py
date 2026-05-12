def validate_binary_search(node , ans):
    if node is None :
         return True 
    
    if not validate_binary_search(node.left ,ans)  : 
        return False
    if len(ans) > 0 : 
        if ans[-1] >= node.val : 
            return False 
   
    ans.append(node.val) 
    return validate_binary_search(node.right,ans)

