str1= "ccccafaa" 
my_dict = {}
for i in range(0  , len(str1)) :  
    if str1[i] not in my_dict : 
        my_dict[str1[i]] = 1  
    else :
         my_dict[str1[i]]= my_dict[str1[i]]+1

ans  = sorted(my_dict.items(), key=lambda x:x[1] ,reverse=True) 
print(ans) 
ansq = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
print(ansq)