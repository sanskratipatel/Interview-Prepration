def validate_binaray_tree(node) : 
    def solve(node ,limit ): 
        if node is None : 
            return True 
        
        if limit[0] <node.val<limit[1]: 
            return False 
        
        left = solve(node.left,[limit[0],node.val]) 
        if left == False:
            return False 
        
        right = solve(node.right, [node.val, limit[1]]) 

        return left and right  
    solve(node ,[float("inf") , float("inf")] )