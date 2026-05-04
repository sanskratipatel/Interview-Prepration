from collections import deque ,OrderedDict
def level_order_traversal(node):
    if node is None : 
        return 
    d = deque([node]) 
    while d  : 
        root = d.popleft() 
        print(root.val , end=" ") 
        if root.left : 
            d.append(root.left) 
        if root.right: 
            d.append(root.right)

def top_view_binary_tree(node) : 
    if node is None : 
        return [] 
    q = deque([node, 0]) 
    my_dict = {} 
    while q : 
        root ,vl  = q.popleft() 
        if vl not in my_dict : 
            my_dict[vl] = root.val 
        
        if root.left : 
            q.append(root.left, vl-1) 
        if root.right :
            q.append(root.right  ,vl+1) 
    return [my_dict[x] for x in sorted(my_dict)]