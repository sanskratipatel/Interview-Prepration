str1 = "character" 
my_dcit = {} 
for i in range(0 , len(str1)) :  
    if str1[i] not in my_dcit : 
        my_dcit[str1[i]] = 1 
    else : 
        my_dcit[str1[i]] = my_dcit[str1[i]]+1 

ans = sorted(my_dcit.items() , key=lambda x : (x[1] , x[0])) 
print(ans)
