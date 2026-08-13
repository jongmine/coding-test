def solution(n):
    answer = []
    
    def hanoi(n, start, end, bypass):
        # 한 개인 경우 즉시 start -> end
        if n == 1:
            answer.append([start, end])
            return
        
        # 1. 출발지의 n-1개를 경유지로 (치우기)
        hanoi(n - 1, start, bypass, end)
        
        # 2. 가장 큰 원판을 목적지로 (이동)
        answer.append([start, end])
        
        # 3. 경유지의 n-1개를 목적지로 (다시 쌓기)
        hanoi(n - 1, bypass, end, start)
    
    hanoi(n, 1, 3, 2)
    return answer