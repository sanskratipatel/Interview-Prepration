str1 = "eiaboooo"
str2 = "ab"
my_dict = {} 

for i in range(0 , len(str2)) :
    if str2[i] not in my_dict: 
        my_dict[str2[i]] = 1
    else : 
        my_dict[str2[i]] =my_dict[str2[i]] +1 

n = len(str2) 
window_dict = {}
i = 0 
j = 0 
is_found = False
while j< len(str1) :  
    print("Here ************** " ,j)
    if str1[j] not in window_dict : 
        window_dict[str1[j]] = 1 
    else : 
        window_dict[str1[j]] = window_dict[str1[j]] + 1 
    if j-i+1 == n :  
        print(my_dict , window_dict)
        if my_dict == window_dict : 
            is_found = True
            break
        window_dict[str1[i]] = window_dict[str1[i]] -1  
        if window_dict[str1[i]] ==0 :
            del window_dict[str1[i]]
        i = i+1 
    j = j +1 

print(is_found)
                
        
                