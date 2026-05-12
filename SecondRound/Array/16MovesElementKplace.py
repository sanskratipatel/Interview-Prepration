def moves_element_k_place(arr , k ) : 
    n = len(arr) 
    rotate = k % n
    for i in range(0 , rotate) :
        e = arr.pop() 
        arr.insert(0 ,e) 
    return arr 


def reverse(nums , right , left) : 
    while left < right : 
        nums[left] , nums[right] = nums[right], nums[left] 
        left = left +1 
        right = right +1 
