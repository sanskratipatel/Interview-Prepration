def contain_with_most_water(arr) : 
    ans = 0 

    for i in range(0 , len(arr)) : 
        for j in range(i+1 , len(arr)) : 
            height = min(arr[i] , arr[j]) 
            width =j - i
            area = height * width 
            ans = max(ans, area)
    return ans 


def contain_with_most_water(arr) : 
    ans = 0 
    left = 0 
    right = len(arr) -1
  
    while left <= right : 
        height = min(arr[left] , arr[right]) 
        width = right -left 
        area = height * width 
        ans = max(ans,area) 

        if arr[left] < arr[right] : 
            left = left+1 
        else : 
            right = right - 1

    return ans