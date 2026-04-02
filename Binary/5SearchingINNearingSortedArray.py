# How Many time Sorted Array Rotated 

arr = [5,10,30,20,40] 

low = 0 
high = len(arr)-1 
count = -1 
n = len(arr)
key = 30
while(low <= high) :
    mid = low + (high -low)//2   
    prev = (mid-n+1)%n
    next_ele = (mid +1)%n 

    if arr[mid]==key: 
        print("Smallest element ", mid , arr[mid])  
        ans = mid 
        break 
    if  key == arr[prev]: 
        ans = prev 
        break 
    
    if key==arr[next_ele] : 
        ans = next_ele 
        break 
    
    elif arr[mid] < key: 
         low = next_ele+1 
    else: 
        high = prev - 1  

