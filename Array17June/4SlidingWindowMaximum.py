arr = [1,3,-1,-3,5,3,6,7] 

k = 3 

i= 0 
j = 0  
ans = [] 
maximum_sum = float("-inf")
sum = 0
while(j < len(arr)) :  
    print("^^^^^^^^^^^^^^^^")
    sum = sum + arr[j]
    if (j-i+1) < k : 
        j = j+1 
    elif (j-i+1) == k :  
        maximum_sum = max(sum , maximum_sum) 
        ans.append(sum) 
        sum = sum-arr[i] 
        i = i +1 
        j = j+1 

print(ans , maximum_sum)

