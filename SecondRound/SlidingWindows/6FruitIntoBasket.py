arr = [3,3,3,1,2,1,1,2,3,3,4] 
my_dict = {} 
count = 0 
max_count = 0 
k =2
i = 0 
j = 0 

while j<len(arr) : 
    if arr[j] not in my_dict :  
        my_dict[arr[j]] = 1 
    else : 
        my_dict[arr[j]] = my_dict[arr[j]] +1  
    if len(my_dict) > k : 
        while len(my_dict) > k : 
            my_dict[arr[i]] = my_dict[arr[i]] -1 
            if my_dict[arr[i]] == 0 : 
                del my_dict[arr[i]] 
            i = i+1
    max_count = max(j-i+1 , max_count) 
    j = j+1

