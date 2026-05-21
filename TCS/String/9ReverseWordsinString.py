str1 = "Hello World" 
ans = str1.split(" ") 
print(type(ans)) 
for i in range(len(ans)) :  
    words = ""
    for j in range(len(ans[i])-1 , -1, -1) :  
        words = words + ans[i][j] 

    ans[i] = words 

print(" ".join((ans)))   
print(ans)