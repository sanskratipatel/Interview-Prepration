# Maximum SubArray 

def maximum_subarray(arr) : 
    maxi = 0
    for i in range(0 , len(arr)) : 
        sum = 0 
        for j in range(i+1 , len(arr)) :   
            sum = arr[j] +sum 
            maxi = max(sum , maxi)

    return maxi


def Kadane_Algorithm(arr) : 
    sum = 0
    max_sum = arr[0] 
    for i in range(0 , len(arr)) :
        max_sum = max(sum , max_sum)  
        sum = arr[i] + sum 
        if sum<0 : 
            sum = 0 
       
    return max_sum