# Find Number that is appear once 

arr = [1,1,2,3,3,4,4] 
# Brute Force 
for i in range(0 , len(arr)):  
    count = 0
    num = arr[i] 

    for j in range(0 , len(arr)) : 
        if arr[j] == num :  
            count = count+1 
    if count == 1 : 
        print("Number appera once is ", num) 
        break


my_dict = {} 
for i in range(0 , len(arr)) : 
    if arr[i] not in my_dict: 
        my_dict[arr[i]] = 1 
    else: 
        my_dict[arr[i]] = my_dict[arr[i]]+1 

ans = 0
for key in my_dict : 
    if my_dict[key] == 1 : 
        ans = key
print(ans)