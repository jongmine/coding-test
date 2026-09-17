def solution(land):
    n = len(land)
    answer = [0]
    
    for i in range(1, n): # 1행부터 마지막행까지 이전행의 최댓값을 찾기
        current_row = [] # 현재행의 값
        for j in range(4):
            prev = land[i - 1][:j] + land[i - 1][j + 1:] # 이전행에서 같은열 제외
            prev_max = max(prev) #
            current_row.append(prev_max + land[i][j]) # 이전행까지 최댓값과 현재행값 계산
            
        land[i] = current_row # 현재행을 누적최댓값으로 갱신
            
    return max(land[-1])