arr =  [0 ,1,2,0,1,2,1,2,0,0,0,1] 

count1 = 0 
count2 = 0 
count3 = 0 

for i in range(0 , len(arr)) : 
    if arr[i] == 0 :
        count1 = count1+1 
    elif arr[i] ==1 :
        count2 = count2+1 
    else:
        count3 = count3 +1 
    

for j in range(0 , count1) : 
    arr[j]  = 0 

n = count2 +count1 
for k in range(count1 , n) : 
    arr[k] = 1 

n2 = n+count3 
for l in range(n , len(arr)) :
    arr[l] = 2 

print(arr)
