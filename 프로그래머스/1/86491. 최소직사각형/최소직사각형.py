# 모든 명함이 통과하는 가로/세로 각각 가장 긴 변 구하기
# 명함을 회전해서 수납할 경우도 고려 -> 가로<->세로
    

def solution(sizes):
        
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        # 회전하는 상황을 고려해서 긴 변과 짧은 변 구하기
        long_side, short_side = max(w, h), min(w, h)
        
        # 편의를 위해 임의로 가장 긴 변을 가로로 고정 -> 면적만 구할거라 상관 X
        w = long_side
        h = short_side
        
        # 기존 최댓값 갱신
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    
    # 면적 반환
    return max_w * max_h