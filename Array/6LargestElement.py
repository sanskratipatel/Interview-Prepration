arr = [32,53,562,4,3,5,35] 
maxi = float("-inf") 

for i in range(0 , len(arr)) : 
    if arr[i] > maxi : 
        maxi = arr[i] 

print(maxi)