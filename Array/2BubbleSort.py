arr = [6,534,12,6,7,3,12] 

for i in range(0 , len(arr)) :
    for j in range(i+1 , len(arr)) : 
        if arr[j] > arr[i] : 
            arr[i] , arr[j] = arr[j] ,arr[i] 
print(arr)