arr = [-2,1,-3,4,-1,2,1,-5,4]  
max_sum = 0 
sum = 0 
for i in range(0 , len(arr)) :  
    sum = sum + arr[i] 
    max_sum = max(sum , max_sum)
    if sum < 0 : 
        sum = 0 
     
    
