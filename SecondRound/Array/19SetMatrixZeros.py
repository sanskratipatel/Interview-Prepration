def set_matrix_zeros (arr =[] ) :
    row = len(arr) 
    col = len(arr[0]) 
    row_track =[0 for i in range(row)] 
    col_track = [0 for i in range(col)] 
    for i in range(0 , row) : 
        for j in range(0 , col) : 
            if arr[i][j] == 0 : 
                row_track[i] = -1 
                col_track[j] = -1 
    
    for i in range(0 , row) :
        for j in range(0 , col) : 
            if row_track[i] ==-1 or col_track[j] == -1 :
                arr[i][j] = 0 
    return arr

