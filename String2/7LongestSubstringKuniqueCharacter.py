str1 = "aabacbebebe" 
my_dict ={} 
i = 0
j = 0 
k = 3
max_size = 0
while(j<len(str1)) : 
    if str1[j] not in my_dict:
        my_dict[str1[j]] = 1  
    else : 
        my_dict[str1[j]] = my_dict[str1[j]]+1 
    if (k) > len(my_dict) :  
        j = j+1 
    elif k < len(my_dict) :  
        while k < len(my_dict) : 
            my_dict[str1[i]] =my_dict[str1[i]]-1 
            if my_dict[str1[i]] ==0 : 
                del my_dict[str1[i]] 
            i=i+1  
        if len(my_dict) == k : 
            max_size = max(max_size , (j-i+1))
        j = j+1 
    else: 
        max_size = max(max_size , (j-i+1)) 
        j = j+1 

print(max_size)


    
