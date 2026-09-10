def solution(brown, yellow):
    answer = []
    s = brown + yellow # brown + yello = 전체칸 = w * h

    # s의 약수들 중 brwon, yello 조건이 맞는지 확인
    # e.g. 12: 12/1, 6/2, 4/3
    
    # for h in range(1, int(s ** 0.5) + 1): # 넓이의 제곱근까지만 확인
    for w in range(1, s + 1): # 넓이의 제곱근까지만 확인
        # w, h가 s의 약수여야 함
        if s % w == 0:
            h = s // w
        
            # 가장자리 2칸을 제외한 w, h의 곲이 yellow 넓이면 정답
            if (w - 2) * (h - 2) == yellow:
                answer = [w, h]
        
    
    return answer