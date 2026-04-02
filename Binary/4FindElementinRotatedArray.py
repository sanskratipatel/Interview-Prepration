# How Many time Sorted Array Rotated 

arr = [11,12,13,14,15,2,3,4,5,6,7,8] 

low = 0 
high = len(arr)-1 
count = -1 
n = len(arr)
ind = -1
while(low <= high) :
    mid = low + (high -low)//2   
    prev = (mid-n+1)%n
    next_ele = (mid +1)%n 

    if arr[mid]<=arr[prev] and arr[mid]<=arr[next_ele] : 
        print("Smallest element ", mid , arr[mid])  
        ind = mid 
        break
    
    elif arr[mid] > arr[prev]: 
         low = mid+1 
    else: 
        high = mid +1  


