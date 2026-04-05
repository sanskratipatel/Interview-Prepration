str1 ="628746"

for i in range(len(str1)-1 , -1, -1): 
    if int(str1[i])%2 !=0 : 
        print(str1[0:i+1]) 
        break 
