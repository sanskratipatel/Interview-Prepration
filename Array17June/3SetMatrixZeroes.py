def set_matrix_zeros(arr) : 
    rows = len(arr) 
    cols = len(arr[0]) 

    col_count =[0] *cols 
    row_count = [0] * rows 
    for i in range(rows) : 
        for j in range(cols) : 
            if arr[i][j] == 0 : 
                row_count[i] = -1 
                col_count[j] = -1 
    

    for i in range(rows) : 
        for j in range(cols) : 
            if row_count[i] == -1 or col_count[j] == -1 : 
                arr[i][j] =0 
                