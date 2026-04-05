# Kadane's Algorithm for Maximum Subarray Sum 

arr =[ 3,-4,5,4,-1,7,-8] 



max_sum = float("-inf")

for i in range(0 , len(arr)) : 
    current_sum = 0
    for j in range(i , len(arr)) : 
        current_sum = current_sum + arr[j] 
        max_sum = max(current_sum , max_sum) 
    
print(max_sum) 


sum_arr = float("-inf") 
current_sum1 = 0 

for i in range(0 , len(arr)) : 
    current_sum1 = arr[i] +current_sum1 
    sum_arr = max(current_sum1, sum_arr) 
    if current_sum1 < 0 : 
        current_sum1 = 0

print(sum_arr) 