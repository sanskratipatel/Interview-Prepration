arr = [12,42,45,64,35,3,74,34,53] 

second_largest = float("-inf") 
largest = float("-inf") 

for i in range(0 , len(arr)) : 
    if arr[i] > largest : 
        second_largest = largest 
        largest = arr[i] 
    elif arr[i] >second_largest and arr[i] < largest :  
        second_largest = arr[i]

print(largest ,second_largest)