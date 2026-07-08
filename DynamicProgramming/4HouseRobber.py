def house_robber(arr) :  
    dp = [0] * len(arr) 
    n = len(arr) 
    def solve(i) :   
        if i == 0 : 
            return arr[i]
        if i < 0 : 
            return 0  
        if dp[i] !=0 : 
            return dp[i] 
        pick = arr[i] + solve(i-2) 
        not_pick = 0 + solve(i-1) 
        dp[i] = max(pick , not_pick) 

        return dp[i] 
    return solve(n-1)


    
    