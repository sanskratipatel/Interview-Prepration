str1 = "forxxorfstefro" 
s ="for" 


j = 0 
my_dict = {}
ans = 0 
for i in range(0 ,len(s)) : 
    if s[i] not in my_dict :
        my_dict[s[i]] = 1 
    else:
         my_dict[s[i]]= my_dict[s[i]]+1
count = len(my_dict) 
i = 0   
while(j<len(str1)) : 
    if str1[j] in my_dict : 
        my_dict[str1[j]] = my_dict[str1[j]]-1 
        if my_dict[str1[j]] ==0 :
            count = count-1
    
    if (j-i+1) < len(s) :
        j  = j+1 
    elif (j-i+1 ) == len(s) :
        if count ==0 :
            ans = ans +1 
        if str1[i] in my_dict : 
            my_dict[str1[i]] = my_dict[str1[i]]+ 1 
            if my_dict[str1[i]] == 1 : 
                 count = count+1 
        j = j+1 
        i = i+1 
print(ans)