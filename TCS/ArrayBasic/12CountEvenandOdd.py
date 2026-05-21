arr = [1, 2, 3, 4, 5, 6] 
even = 0 
odd = 0
for i in range(0 , len(arr)) : 
    if arr[i] % 2== 0 : 
        even = even +1 
    else : 
        odd = odd +1 
print(odd , even) 
