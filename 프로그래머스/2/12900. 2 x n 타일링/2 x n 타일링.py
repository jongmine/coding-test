def solution(n):
    
    dp = {0:1, 1:1, 2:2}
    
    for i in range(3, n + 1):
        
        
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    
    return dp[n]


# 점화식
# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(n) = f(n-1) + f(n-2)
