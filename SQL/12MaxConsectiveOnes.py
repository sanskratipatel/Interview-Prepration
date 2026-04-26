def max_consective_onces(arr) : 
    maxi=0
    for i in range(0 , len(arr)) :
        key = 0
        for j in range(i , len(arr)) :
            if arr[j] == 0 :
                key = key+1 
            if key > 2 : 
                break
            maxi = max(maxi , j-i+1) 
    print(maxi)


def consective_ones(arr) : 
    maxi = 0  
    key = 0 

    i = 0 
    j = 0 
    while (j <len(arr)) : 
        if arr[j] == 0: 
            key = key+1
        while(key >2) : 
            if arr[i] == 0 :
                key = key -1  
            i = i+1 
  
        maxi = max(maxi, j-i+1)  
        j = j+1 
    print(maxi) 
arr = [1,1,0,1,0,1,1,1]
consective_ones(arr)
max_consective_onces(arr)