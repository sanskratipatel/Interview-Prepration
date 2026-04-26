from collections import deque
def height_binary_tree_recursive(node): 
    if node is None: 
        return 0 
    leftHeight = height_binary_tree_recursive(node.left) 
    rightHeight = height_binary_tree_recursive(node.right) 
    return 1 +max(leftHeight ,rightHeight) 



def height_binary_tree(node): 
    queue = deque([]) 
    result =[] 
    queue.append(node) 

    while(len(queue) != 0) :  
        e = queue.popleft() 
        result.append(e.val)  
        if e.left is not None :
            queue.append(e.left) 
        if e.right is not None:
            queue.append(e.right)
    return result


def height_binary_tree_iterator(node): 
    queue = deque([]) 
    result =[] 
    queue.append(node)  
    height = 0

    while(len(queue) != 0) :  
        level_size = len(queue)  
        height = height +1 

        for i in range(level_size) : 
                e = queue.popleft() 
                if e.left is not None : 
                    queue.append(e.left)  
                if e.right is not None: 
                    queue.append(e.right) 
    return height 



def againg(node) : 
    qeue= deque([]) 
    qeue.append(node) 
    height = 0
    while(len(qeue) != 0 ) :  
        level = len(qeue) 
        height = height +1 

        for i in range(level) : 
            e = qeue.popleft() 
            if e.left is not None : 
                qeue.append(e.left) 
            if e.right is not None : 
                qeue.append(e.right) 


      


def height_2 (node) :
    if node is None :
        return 
    left = height_2(node.left) 
    right = height_2(node.right) 

    return 1 + max(left, right)