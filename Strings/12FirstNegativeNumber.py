# Find first negative number of size k window in an array 

arr = [12, -1, -7, 8, -15, 30, 16, 28] 
k = 3 
i = 0 
j = 0 
a = []
result = [] 
while(j<len(arr) ): 
    if arr[j] < 0 : 
        a.append(arr[j])  
    
    if (j-i+1) <k : 
        j = j+1 
    elif (j-i+1) == k : 
        if len(a) == 0 : 
            result.append(0) 
        else: 
            result.append(a[0]) 
            if a[0] == arr[i] :
                a.pop(0) 
        i = i+1 
        j = j+1
print(result)