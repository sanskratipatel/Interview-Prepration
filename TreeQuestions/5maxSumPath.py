def max_path(node) : 
    sum = float("-inf") 
    def solve(node) : 
        nonlocal sum 
        if node is None : 
            return 0 

        left_s = solve(node.left) 
        if left_s < 0 : 
            left_s = 0 
        right_s = solve(node.right) 
        if right_s < 0 : 
            right_s = 0 
        
        sum = max(sum ,left_s +right_s + node.val) 
        return node.val + max(right_s ,left_s) 

    solve(node ) 
    return sum  