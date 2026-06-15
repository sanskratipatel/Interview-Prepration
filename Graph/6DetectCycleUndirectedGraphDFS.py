def isCycle(v, edges) : 
    adj_lst = [[] for _ in range(v)] 
    for u , v in edges : 
        adj_lst[u].append(v) 
        adj_lst[v].append(u) 
    visited = [0] * v  
    for i in range(0 ,v) : 
        if visited[i] == 1 : 
            continue 
        queue = deque() 
        queue.append((i,-1)) 
        visited[i] =1 
        while len(queue) != 0 : 
            node ,parent = queue.popleft() 
            for adjNode in adj_lst[node] : 
                if visited[adjNode] == 0 :
                    visited[adjNode] =1 
                    queue.append(adjNode, node) 
                else : 
                    if adjNode != parent : 
                        return True 
    return False