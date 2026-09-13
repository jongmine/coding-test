import sys
sys.setrecursionlimit(200000)


def solution(n):
    
    memo = {
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5
    }
    
    def fibonacci(n, memo):
        
        # memo에 해당 값이 있다면 계산 하지 않고 반환 -> 재귀 오류 방지
        if n in memo:
            return memo[n]
        
        # 점화식: F(n) = F(n-2) + F(n-1)
        answer = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)
        memo[n] = answer
        
        return answer % 1234567
    
    return fibonacci(n, memo)
