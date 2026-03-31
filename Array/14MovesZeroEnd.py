nums =[0,1,2,0,3,2,0,46,4,7,2,0,0] 
result = [] 
count = 0 
for i in range(0 , len(nums)) : 
    if nums[i] != 0 : 
        result.append(nums[i]) 
    else :  
        count = count +1 


for i in range(0, count) : 
    result.append(0)

print(result) 

if len(nums) >1 : 
    i = 0 
    while(i< len(nums)) : 
        if nums[i]==0 :
            break 
        i = i+1 
        if i == len(nums) :  
            break 
    j = i+1  
    while(j<len(nums)):
        if nums[j]!= 0 : 
            nums[i] , nums[j] = nums[j] , nums[i]
            i = i+1 
        j = j+1 
        
