def K_th_smallest_largest_element(node ,ans) : 
    if node is None :
        return ans 
    
    left = K_th_smallest_largest_element(node.left ,ans) 
    ans.append(node.val) 
    right = K_th_smallest_largest_element(node.right ,ans) 

ans = []
K_th_smallest_largest_element(node , ans) 

ele = 3 
print(ans[ele-1])