# 재귀 호출 깊이 제한 증가
# import sys
# sys.setrecursionlimit(10 ** 6)


def solution(n):
    # memorization for DP
    memo = {
        0: 0,
        1: 1,
        2: 1
    }
    
# 1. 재귀    
#     def fibonacci(n, memo):
#         if n in memo:
#             return memo[n] % 1234567
        
#         # 점화식: F(n) = F(n-2) + F(n-1)
#         answer = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)
#         memo[n] = answer
        
#         return answer % 1234567
    
#     return fibonacci(n, memo)
    
    # 2. 반복문        
    for i in range(3, n + 1):
        memo[i] = memo[i - 2] + memo[i - 1]    
    return memo[i] % 1234567
