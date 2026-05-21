arr = [1,1,0,0,6,3,1,1,1,0,6,1,2,1,1,1,1] 
max_count = 0
count = 0

for i in range(0 , len(arr)) : 
    if arr[i] == 1 : 
        count = count +1 
    else : 
        max_count = max(max_count , count) 
        count = 0  

max_count = max(max_count , count)