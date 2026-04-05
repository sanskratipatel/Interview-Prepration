s = "anagram"
t = "nagaram" 

s1 = sorted(s) 
t1 = sorted(t) 
if s1 == t1 : 
    print("true")
else :
    print("false") 


my_dict = {} 

for i in range(0 , len(s)) : 
    if s[i] not in my_dict: 
        my_dict[s[i]] = 1 
    else :
        my_dict[s[i]] = my_dict[s[i]] + 1 

for j in range(0 , len(t)): 
    if t[j] not in my_dict : 
        print("false")
        break 
    else : 
        my_dict[t[j]] = my_dict[t[j]] - 1 
        if my_dict[t[j]] == 0 : 
           del my_dict[t[j]]  

if len(my_dict) == 0 :
    print("true")
else :
    print("false")