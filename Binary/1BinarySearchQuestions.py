arr = [1,2,3,4,5,6,7,8] 
low = 0 

high = len(arr)-1 
key = 8 
while(low <= high) : 
    mid = low + (high - low)//2 

    if arr[mid] == key :
        print("Ans at index" , mid) 
        break 
    elif arr[mid] > key : 
        high = mid -1 
    else: 
        low = mid +1 
        