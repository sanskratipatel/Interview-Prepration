arr = [1,2,3,4,5,6,7,8] 
low = 0 

high = len(arr)-1 
key = 18 
ans = -1
while(low <= high) : 
    mid = low + (high - low)//2 

    if arr[mid] == key : 
        ans = mid
        print("Ans at index" , mid) 
        break 
    elif arr[mid] > key : 
        high = mid -1 
    else: 
        ans = mid
        low = mid +1 
print(ans)