str1 = "abcabedqasfsca"

i = 0 
j = 0 
my_dict = {} 
max_size = 0
while(j < len(str1)) :
    if str1[j] not in my_dict:
         my_dict[str1[j]] = 1 
    else :   
        while(str1[j] in my_dict ) :
            my_dict[str1[i]] =  my_dict[str1[i]]-1 
            if  my_dict[str1[i]]== 0 :
                del  my_dict[str1[i]] 
            i = i+1 
       
        my_dict[str1[j]] = 1  
    max_size = max(max_size , j-i+1) 
    j = j+1   
    
print(max_size)