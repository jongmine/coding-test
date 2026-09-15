def solution(n):
    
    answer = [0, 1, 2]
    for i in range(3, n + 1):
        answer.append(answer[i - 1] + answer[i - 2])
        
    return answer[n] % 1234567


# 점화식 찾기
# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5 # 1111 
# f(5) = 8 # 11111 2111 1211 1121 1112 221 212 122
# ...
# f(n) = f(n-1) + f(n-2)
