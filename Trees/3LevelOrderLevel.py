
from collections import deque
def level_order_traversal(node) : 
    q1  = deque([]) 
    q1.append(node)  
    res = []
    for i in range(0 , len(q1)) : 
        e =q1.popleft()  
        res.append(e.val) 

        if e.left is not None : 
            q1.append(e.left) 
        if e.right is not None: 
            q1.append(e.right) 

        
