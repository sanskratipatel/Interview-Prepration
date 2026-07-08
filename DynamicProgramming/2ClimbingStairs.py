def climbing_stairs(cost) : 
    dp = [0] * lrn(cost) 
    def solve(i):
        if i <2 : 
            return cost[i] 
        if dp[i] != 0 : 
            return dp[i] 

        dp[i] = cost[i] + min(solve(i-1) ,solve(i-2))  
        return dp[i]
    return min(solve(n-1) , solve(n-2))