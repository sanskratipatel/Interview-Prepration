def frog_jump(arr) : 
    dp = [0] * len(arr)
    def solve(i) : 
        if i == 0 : 
            return 0  
        jump1 = solve(i-1) + abs(arr[i] - arr[i-1])  
        if i>1 :
             jump2 = solve(i-2) + abs(arr[i] - arr[i-2]) 
        else : 
             jump2 = float("inf")
        return min(jump1 , jump2) 


def frog_jump(arr) : 
    dp = [0] * len(arr)
    def solve(i) : 
        if i == 0 : 
            return 0   
        if dp[i] != 0 : 
            return dp[i]
        jump1 = solve(i-1) + abs(arr[i] - arr[i-1])  
        if i>1 :
             jump2 = solve(i-2) + abs(arr[i] - arr[i-2]) 
        else : 
             jump2 = float("inf")
        dp[i] = min(jump1 , jump2)  
        return dp[i]
