grid = [[9,1,7] ,[8,9,2],[3,4,6]] 

n= len(grid) 
seen = set()  
repeating = -1 
for row in grid : 
    for i in row :
        if i in seen : 
            repeating = i 
        else : 
            seen.add(i)
miss = -1
for j in range(0 , n*n+1) :
    if j not in seen:
        miss = j
    
print(miss , repeating)