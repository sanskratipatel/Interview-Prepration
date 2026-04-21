s1 = "cadbzabcd" 
max_length = 0
for i in range(0 , len(s1)) :
    my_dict = {}
    for j in range(i+1 , len(s1)) :  
        if s1[j] not in my_dict :
            my_dict[s1[j]] = 1   
            len1 = j-i+1
            max_length = max(max_length , len1)
        else : 
            break 

print(max_length)