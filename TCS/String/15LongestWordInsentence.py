str1 = "wqew ewertyuwerrwewerws esdfsdfsdf erfsgedgsegdfs" 
s = str1.split(' ') 
max_length = 0 
ans = ""
for i in range(len(s)) : 
    if max_length < len(s[i]):
       max_length = max(max_length ,len(s[i]) )  
       ans = s[i]
print(ans) 
print(' '.join(s))