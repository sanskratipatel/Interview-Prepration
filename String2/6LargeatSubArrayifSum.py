arr = [4,1,1,4,1,2,3,5,1,3,5] 
i = 0 
j = 0 
target =6
sum = 0
max_len = 0
while(j<len(arr)) : 
   
    sum = sum+ arr[j]  
    if sum <target : 
        j = j+1
    elif (target) < sum  : 
        while(target) <sum:
            sum = sum- arr[i] 
            i = i+1 
        if sum == target : 
            max_len = max(j-i+1 , max_len) 
        j = j+1 
    else :
        max_len = max(j-i+1 , max_len) 
        j = j+1 
print(max_len)