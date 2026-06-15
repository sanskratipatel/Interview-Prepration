def flood_fills(image, sr, sc, newColor) :  
    if image[sr][sc] == newColor : 
        return image 
    rows = len(image) 
    cols = len(image[0]) 
    intial_color = image[sr][sc]
    def dfs(i , j ,rows , cols , newColor, images ,intial_color) :  
        if i < 0 or i >= rows or j < 0 or j >= cols : 
            return 
        if image[i][j] != intial_color : 
            return 
        if image[i][j] == newColor : 
            return 
        image[i][j] = newColor 
        dfs(i+1 , j ,rows,cols ,newColor, images ,intial_color) 
        dfs(i , j+1 ,rows,cols ,newColor, images ,intial_color)  
        dfs(i-1 , j ,rows,cols ,newColor, images ,intial_color) 
        dfs(i , j-1 ,rows,cols ,newColor, images ,intial_color) 
    dfs(sr ,sc ,rows , cols , newColor, images ,intial_color)