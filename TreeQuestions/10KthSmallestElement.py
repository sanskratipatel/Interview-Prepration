def in_order_solution(node ,ans) : 
    if node is None :  
        return 
    in_order_solution(node.left, ans) 
    ans.append(node.val)
    in_order_solution(node.right, ans)  
    return ans 

def answer(node,k ) :
    ans = []
    in_order_solution(node , ans )  
    return ans[k-1]

