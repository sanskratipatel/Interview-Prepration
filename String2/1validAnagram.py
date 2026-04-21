s1 = "anagraim" 
s2 = "nagarahm" 
# For brute force just sort both string and compare them
if len(s1) != len(s2) : 
    print("Not Anangram") 
else:
    s1 = sorted(s1) 
    s2 = sorted(s2) 

    if s1 == s2 :
        print("anagram") 
    else:
        print("Not Anagram")  

# For optimal Solution using dict 
if len(s1) != len(s2) : 
    print("Not Anangram") 
else:
    my_dict = {} 
    for i in range(0 , len(s1)) :
        if s1[i] not in my_dict :
            my_dict[s1[i]] = 1 
        else:  
             my_dict[s1[i]] =  my_dict[s1[i]] +1 
    is_ana = True
    for i in range(0 , len(s2)) : 
        if s2[i] not in my_dict : 
            print("Not Anagram")  
            is_ana = False
            break
        elif s2[i] in my_dict : 
            my_dict[s2[i]] =  my_dict[s2[i]]-1  
            if my_dict[s2[i]] ==0 :
                del my_dict[s2[i]] 

    if is_ana == True :
        print("Yess anagram")
