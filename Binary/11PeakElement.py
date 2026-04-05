arr = [0,3,8,9,5,2] 

low = 0 
high = len(arr) -1 
n = len(arr)
while( low<= high) : 
    mid = low + (high-low) //2 
    prev = (mid+n-1)%n 
    next_ele = (mid+1)%n 

    if arr[mid] >= arr[prev] and arr[mid] >= arr[next_ele] : 
        print("PEAK ELEMENT IS = " , arr[mid]) 
        break 
    elif arr[mid] <= arr[prev] :
        high = mid -1
    else:      
        low = mid + 1 