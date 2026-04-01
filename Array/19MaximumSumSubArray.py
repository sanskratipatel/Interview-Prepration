arr = [1,2,3,1,1,1,1,4,2,3] 
k = 3 

sum = 0 
i = 0 
j = 0  
maxi = float("-inf")
while(j < len(arr)) : 
    sum = sum + arr[j] 
    if (j-i+1) < k : 
        j = j+1 
    elif (j-i+1) ==k :  
        maxi = max(sum , maxi) 
        sum = sum - arr[i] 
        i = i+1 
        j = j+1 
    
print(maxi)
# Two pointer 
