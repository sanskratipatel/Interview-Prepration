s = " the   sku    is blue " 

s  = s.strip() 

arr = s.split() 
ans = ""

for i in range(len(arr)-1, -1, -1) : 
    if arr[i] !=  "": 
       
       ans = ans + arr[i] + " " 
print(ans.strip())