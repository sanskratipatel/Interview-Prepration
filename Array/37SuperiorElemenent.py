arr = [1,2,3,2] 
in_max = float("-inf")
ans = []
for i in range(len(arr)-1,-1,-1) : 
    if arr[i]> in_max : 
        in_max = max(in_max,arr[i])
        ans.append(in_max)
 
print(sorted(ans)) 

for i in range(0 , len(arr))  : 
    maxi = True 
    for j in range(i+1 , len(arr)) : 
        if arr[j] > arr[i] :
            maxi = False 
            break 
    if maxi == True : 
        print(arr[i])
    

