def solution(x, y, n):
    dp = [1000001] * (y + 1)
    dp[x] = 0 # 시작점 x 연산 횟수
     
    for i in range(x, y + 1):
        # 시작점 x에서 도달할 수 없는 숫자
        if dp[i] == 1000001:
            continue
            
        # 현재 i에서 연산 가능한 경우 연산횟수 저장
        
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
            
    # y로 변환하기 위해 필요한 최소 연산횟수
    return dp[y] if dp[y] != 1000001 else -1


# 점화식
# x + n, x * 2, x * 3 / 
# x:2 n:5 -> y:5
# f(1) = -1
# f(2) = 0
# f(3) = -1
# f(4) = 1
# f(5) = -1