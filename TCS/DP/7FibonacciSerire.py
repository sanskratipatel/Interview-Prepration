# def fib_nacci(num) : 
#     if num ==0 or num == 1 : 
#         return num 
#     return fib_nacci(num-1) + fib_nacci(num -2) 
nums = 5
arr = (nums + 1) * [-1]
def fibo2(nums , arr) :   
    if nums ==0  or nums ==1 : 
        return nums 
    if arr[nums] != -1 : 
        return arr[nums]
    arr[nums] = fibo2(nums-1 , arr) + fibo2(nums-2,arr) 
    return arr[nums]

def fibo(nums) : 
    dp = nums+1 *[-1]
    if nums ==0 or nums == 1 : 
        return nums 
    for i in range(2, nums+1) : 
       dp[i] = dp[i-1] + dp[i-2]
    return dp[nums]