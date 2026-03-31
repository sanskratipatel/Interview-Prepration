arr = [ 1,2,4,5,6] 
n = len(arr)
is_desc = True
if arr[0] > arr[n-1] : 
    for i in range(0 , len(arr)-1) :  
         if arr[i] < arr[i+1] : 
              is_desc = False

is_asc = True
if arr[0] < arr[n-1] : 
   
    for i in range(0 , len(arr)-1) :  
         if arr[i] > arr[i+1] : 
              is_asc = False 
print(is_asc , is_desc)
 