arr = [1,2,3,4,5,6,6,7,8,9] 

low = 0 
high = len(arr) -1 
key = 6
res = -1
# Finding First Occurance  
while(low <= high) : 
    mid = low + (high - low) //2 
    if arr[mid] == key : 
        res = mid 
        high = mid -1 
    elif arr[mid] > key : 
        high = mid -1 
    else:  
        low = mid +1

low = 0 
high = len(arr) -1 
res1 =-1
while(low <= high) : 
    mid = low + (high - low) //2 
    if arr[mid] == key : 
        res1 = mid 
        low = mid + 1 
    elif arr[mid] > key : 
        high = mid -1 
    else:  
        low = mid +1 
print(res , res1)

# count 
ans = (res1-res) +1 
print(ans)