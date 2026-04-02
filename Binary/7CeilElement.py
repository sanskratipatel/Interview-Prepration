arr = [2,3,4,5,6,7,8] 
low = 0 

high = len(arr)-1 
key =  1
ans = -1
while(low <= high) : 
    mid = low + (high - low)//2 

    if arr[mid] == key : 
        ans = mid
        print("Ans at index" , mid) 
        break 
    elif arr[mid] > key : 
        ans = mid
        high = mid -1 
    else: 
        
        low = mid +1 
print(ans)