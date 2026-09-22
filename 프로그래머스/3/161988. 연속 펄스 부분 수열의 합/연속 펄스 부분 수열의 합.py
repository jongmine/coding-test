def solution(sequence):
    # 2가지 펄스 수열 경우의 수 고려하여 수열의 합 배열 0번째 값 초기화
    sum1 = sequence[0]  # 1,-1,1,-1,...
    sum2 = -sequence[0] # -1,1,-1,1,...
    answer = max(sum1, sum2) # 정답 초기화
    
    for i in range(1, len(sequence)):
        val = sequence[i]
        
        # 이전 수열을 계속 이어 붙일 것인지 or 
        # 이전 수열이 작아 끊어버리고 여기서부터 새로 시작할 것인가?
        # 부호 교차를 위해 sum1 <-> sum2
        sum1, sum2 = max(val, val + sum2), max(-val, -val + sum1)
        answer = max(answer, sum1, sum2)
        
    return answer