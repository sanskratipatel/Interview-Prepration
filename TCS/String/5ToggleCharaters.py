str1 = "Hello" 
ans = ""
for i in range(0 , len(str1)) : 
    if str1[i].isupper() : 
        ans =ans + str1[i].lower() 
    elif str1[i].islower() : 
        ans = ans+str1[i].upper() 
print(ans)