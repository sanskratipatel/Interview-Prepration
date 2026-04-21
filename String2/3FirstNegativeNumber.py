arr = [2,-4,1,-5,2,-4,2,-3,7,3,2] 
k = 3
ans = []
for i in range(0 , len(arr)-k+1) :
    found = False 
    for j in range(i,i+k):
        if arr[j] < 0 : 
            ans.append(arr[j]) 
            found = True
            break
    if not found :
        ans.append(0) 
print(ans)
neg = []
res = [] 
i = 0 
j = 0 

while(j<len(arr)) :
    if arr[j] < 0 :
        neg.append(arr[j]) 
    if j-i+1 <k : 
        j = j+1 
    elif j-i+1 == k:  
        if len(neg) > 0 : 
           res.append(neg[0])  
           if neg[0] == arr[i] : 
                neg.pop(0)  
        else: 
            res.append(0)
        i = i+1 
        j = j+1  
print(res)
