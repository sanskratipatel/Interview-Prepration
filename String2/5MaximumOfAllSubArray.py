arr = [1,3,-1,-3,5,3,6,7]
k = 3
i = 0 
j = 0 
maximum = 0 
a1 =[]
ans = []
while(j<len(arr)) : 
    while(len(a1) > 0 and arr[j] >a1[0]):
        a1.pop(0)   
    a1.append(arr[j]) 
    
    if (j-i+1 < k): 
        j = j+1 
    elif (j-i+1 == k) :
        ans.append(a1[0]) 
        if len(a1) >0 and a1[0] == arr[i] : 
            a1.pop(0) 
        i = i+1 
        j = j+1 

print(ans)