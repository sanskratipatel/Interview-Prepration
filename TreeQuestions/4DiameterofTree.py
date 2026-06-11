def diameter_of_tree(node) :  
    dia = 0 
    def solve(node , dia) : 
        if node is None : 
            return 0 
        
        left_h = solve(nod.left , dia) 
        right_h = solve(node.right, dia)  
        dai = max(dia , left_h + right_h) 
        return 1 + max(left_h , right_h) 
    return dia


