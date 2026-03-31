arr = [1,1,0,1,1,1,0,1,1,1,1]

maxi = 0
count = 0  
for i in range(0 , len(arr)) : 
    
    if arr[i] == 1 :  
        count = count +1 
        maxi = max(count, maxi) 
    else : 
        count = 0  
maxi = max(count , maxi) 
print(maxi)