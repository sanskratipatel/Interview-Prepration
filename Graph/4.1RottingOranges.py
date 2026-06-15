def rotting_orderanges(grid) : 
    rows = len(grid) 
    cols = len(grid[0]) 
    queue = deque() 
    fresh_count = 0 
    minutes = 0 
    for i in range (rows) : 
        for j in range ( cols) : 
            if grid[i][j] ==2 :
                queue.append((i,j)) 
            elif grid[i][j] == 1 : 
                fresh_count = fresh_count +1 
    
    while len(queue) > 0 and fresh_count >0 : 
        minutes = minutes +1 
        total_round = len(queue) 
        for _ in range (total_round) : 
            i , j = queue.popleft() 
            for dx , dy in ([1,0],[-1,0],[0,-1],[0,1]) : 
                new_i , new_j =dx+i , dy+ j 
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols : 
                    continue 
                if grid[new_i][new_j] ==0 or grid[new_i][new_j] ==2 : 
                    continue 
                grid[new_i][new_j] =2 
                queue.append((new_i,new_j)) 
                fresh_count = fresh_count -1 
    if fresh_count > 0 :
        return -1 
    return minutes