def path_sum(node, target, path, ans):
    if node is None:
        return
    
    path.append(node.val)
    
    # Leaf node
    if node.left is None and node.right is None:
        if sum(path) == target:
            ans.append(path[:])  # copy
    else:
        path_sum(node.left, target, path, ans)
        path_sum(node.right, target, path, ans)
    
    path.pop()  # backtrack