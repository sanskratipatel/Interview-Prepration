nums = [10,5,3,6] 
k = 100 

product = 1 
max_product = 1
i = 0 
j = 0 
while j < len(nums) : 
    product = product * nums[j]
    if product >= k: 
        while product >= k and i<= j :
             product = product // nums[i] 
             i = i+1 
    max_product = max(product , max_product)  
    j = j+1 


