arr = [1,12,-5,-6,50,3] 

sum = 0 
max_avg = float("-inf")
k = 3
i = 0  
j = 0  
while j < len(arr) : 
    sum = sum + arr[j] 
    if j-i+1 < k : 
        j = j+1 
    elif j -i+1 == k : 
        avg = sum / k
        max_avg = max(max_avg , avg) 
        sum = sum - arr[i] 
        i = i+1 
        j = j +1 
