str1 = "12ertdfg245SFD" 
ans = 0

for i in range(len(str1)) : 
    if str1[i].isalpha() : 
        continue 
    else : 
        ans = ans * 10 + int(str1[i])