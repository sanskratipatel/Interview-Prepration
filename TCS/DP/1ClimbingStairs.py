def climbing_stair(nums) : 
    if nums == 0 or nums ==1 : 
        return 1 
    return climbing_stair(nums-1 ) + climbing_stair (nums-2) 

nums = 5
rr = []
arr = (nums +1) * -1

def climbing_stair2(nums , arr) : 
    if nums == 0 or nums == 1 : 
        return 1 
    if arr[nums] != -1 : 
        return arr[nums] 
    arr[nums] = climbing_stair2(nums-1 , arr) + climbing_stair2(nums-2, arr) 
    return arr[nums] 

def climbing_strais3(nums) : 
    arr = (nums +1) * [0]
    
    for i in range(2 , nums+1) : 
        arr[i] = arr[i-1] * arr[i-2] 

    return arr[nums]