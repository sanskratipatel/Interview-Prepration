str1 = "eidbaooo" 
str2 = "ab" 

my_dict = {} 

for i in range(len(str2)) : 
    if str2[i] in my_dict : 
        my_dict[str2[i]] = my_dict[str2[i]] +1 
    else : 
         my_dict[str2[i]] =1
         
window = {} 

for i in range(len(str2)) : 
    if str1[i] in window : 
        window[str1[i]] = window[str1[i]] +1 
    else : 
         window[str1[i]] =1 
# IMPORTANT CHECK
if window == my_dict:
    print(True)
else:
        
    k =len(str2)
    for i in range(k , len(str1)) : 
        if str1[i] in window : 
            window[str1[i]] =  window[str1[i]] +1 
        else : 
            window[str1[i]] = 1  
        left_char = str1[i-k] 
        window[left_char] =window[left_char] -1 

        if  window[left_char] == 0 : 
            del  window[left_char]
        
        if window == my_dict : 
            print(True) 
            break
    else : 
        print(False)
        

        
