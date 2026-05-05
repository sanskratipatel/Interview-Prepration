def is_sorted(arr,n ) :
    if n==0 or n==1 : 
        return True 
    return arr[n-1] > arr[n-2] and is_sorted(arr,n-1) 


arr=[1,2,3,4,95,6] 

n = len(arr) 
print(is_sorted(arr,n))