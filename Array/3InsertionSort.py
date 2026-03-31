arr = [6,4,24,53,5,73,14] 

for i in range(0 , len(arr)) : 
    key = arr[i] 
    j = i-1 
    while( j> 0 and arr[j] >key):  
        arr[j+1] = arr[j]  
        j = j-1 
    

    arr[j+1] = key