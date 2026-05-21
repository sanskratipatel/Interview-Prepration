str1 = "character" 
ans = "" 

for i in range(0 , len(str1)) : 
    if str1[i] not in ans :
        ans = ans+str1[i] 

print(ans)