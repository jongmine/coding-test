def solution(data, col, row_begin, row_end):
    # 0번째 col: PK
    # col번째 값 오름차순 -> PK 내림차순 정렬
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    
    # s_i = sum(data[i][j] % i) 
    hashed = 0
    for r in range(row_begin - 1, row_end):
        s_i = 0
        for c in range(len(data[0])):
            # 각 행 튜플의 값 % i의 합
            s_i += sorted_data[r][c] % (r + 1)
        
        # 모든 s_i들을 XOR 누적
        hashed ^= s_i
            
    return hashed
    