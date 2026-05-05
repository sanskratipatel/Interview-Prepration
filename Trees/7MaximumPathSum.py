def main_function() : 
    maxi = float("-inf")
    def solve(node, maxi) : 
        if node is None:
            return 0 
        ls = solve(node.left) 
        if ls <0 : 
            ls =0 
        rs = solve(node.right) 
        if rs < 0 :
            rs = 0
        maxi = max(maxi , ls+ node.val+rs) 

        return node.val + max(ls,rs) 