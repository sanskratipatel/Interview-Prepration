# from collections import deque
# def level_order_traversal(node) :  
#     if node is None : 
#         return 
#     q = deque([node]) 

#     while q : 
#         ans = q.popleft()
#         print(ans.val , end=" ") 
#         if ans.left is not None : 
#             q.append(ans.left) 
#         if ans.right is not None: 
#             q.append(ans.right) 


from collections import deque 

def level_order_traversal(node) : 
    if node is None :
        return 
    d = deque([node]) 

    while d : 
        n1 = d.popleft() 
        print(n1.val , end=" ") 
        if n1.left is not None : 
            d.append(n1.left) 
        if n1.right is not None : 
            d.append(n1.right)