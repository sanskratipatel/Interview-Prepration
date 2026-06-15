
def solve(num,dp):
    def fib(num) :
        if num == 0 or num ==1 : 
            return num
        if dp[num] != -1: 
            return dp[num]
        dp[num] =  fib(num-1) + fib(n-2)  
        return dp[num]

dp = [-1] * (n-1) 
dp[0] = 0 
dp[1] = 1 

for num in range(2, n+1) : 
    dp[num] = dp[num-1] + dp[num-2] 
return dp[n]