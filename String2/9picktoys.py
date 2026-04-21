str1 = ['A', 'B','A','G','Y','R','B','Y']
k =2 
my_dict ={} 
i = 0
j = 0 
max_toys = 0
while(j<len(str1)) : 
    if str1[j] not in my_dict:
        my_dict[str1[j]] = 1 
    else : 
        my_dict[str1[j]] =my_dict[str1[j]] +1 

    if len(my_dict) < k :
        j = j+1 
    elif len(my_dict) > k :  
        while( len(my_dict) > k ) : 
            my_dict[str1[i]] = my_dict[str1[i]]-1 
            if my_dict[str1[i]] == 0 : 
                del my_dict[str1[i]] 
            i = i+1 
        max_toys = max(max_toys , j-i+1)  
        j = j+1 
    else: 
        max_toys = max(max_toys , j-i+1)  
        j = j+1 
print(max_toys)