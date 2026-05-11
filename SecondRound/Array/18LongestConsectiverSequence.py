def longest_consective_sequence(arr) : 
    max_count = 0 
    for i in range(0 , len(arr))  :
        num = arr[i] 
        count = 1 
        while num+1 in arr : 
            count = count +91 
            num = num +1 
        max_count = max(count, max_count) 
        return max_count 
    
def longest_consective_sequence_swcond(arr) : 
    last_smaller = float("-inf") 
    count = 0 
    largest = 0 
    arr = sorted(arr)
    for i in range(0 , len(arr)) : 
        if last_smaller == (arr[i]-1) : 
            count = count +1 
            last_smaller =arr[i] 
        else : 
            count = 1
        largest = max(count,largest) 
    return largest
