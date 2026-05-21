arr =  [1,2,3,4,5,6] 
mini = float("inf") 
maxi = float("-inf") 

for i in range(0 , len(arr)) : 
    if arr[i] > maxi : 
        maxi = arr[i] 
    if arr[i] < mini : 
        mini = arr[i] 
print(mini , " " , maxi)