nums = [3,1,5,3,6,4,74,6,24] 

def merge_sorted_array(left , right) : 
    i = 0 
    m = len(left) 
    j = 0 
    n = len(right) 
    result = []
    while (i <m and j <n) :  
        if left[i] <= right[j] : 
            result.append(left[i]) 
            i = i+1 
        else: 
            result.append(right[j]) 
            j = j+1 
    if i < m : 
        while(i < m) : 
            result.append(left[i])  
            i = i+1 
    if j < n : 
        while(j<n) : 
            result.append(right[j])
            j = j+1 

    return result
def merge_sort(arr):  
    if len(arr) <= 1 : 
        return arr 
    mid = len(arr)//2 
    left_side = arr[:mid] 
    right_side = arr[mid:] 
    left_sort  = merge_sort(left_side) 
    right_sort = merge_sort(right_side) 
    return merge_sorted_array(left_sort,right_sort) 


print(merge_sort(arr=nums)) 
