def solution(board):
    row = len(board)
    col = len(board[0])
    
    # 가장 큰 정사각형의 변의 길이
    max_side = 0

    # 위, 왼쪽, 왼쪽위 탐색
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                continue
            
            # 인덱스 유효성 검사
            if i >= 1 and j >= 1:
                # 왼쪽, 위, 왼쪽위 중 작은값+1로 갱신
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                
            # 가장 큰 변의 길이 갱신
            max_side = max(max_side, board[i][j])
                
    # 넓이
    return max_side ** 2
