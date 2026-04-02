arr = ['a','f','y','w', 'e'] 
key = 'y'
low = 0 
high = len(arr) -1 
ans = ""
while(low <= high) : 
    mid = low + (high -low)//2 
    if arr[mid] == key : 
        low = mid + 1 
    elif arr[mid] > key : 
        high = mid -1 
    else:
        ans = arr[mid] 
        low = mid +1  
print(ans)
