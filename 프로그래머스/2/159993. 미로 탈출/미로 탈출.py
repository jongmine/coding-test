from collections import deque

# 최대한 빠르게 탈출 -> BFS 이용
# 레버와 문 모두 찾아야 함
# S : 시작 지점 / E : 출구 / L : 레버 / O : 통로 / X : 벽
def solution(maps):
    m, n = len(maps), len(maps[0])
    
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def bfs(row, col, target):
        visited = [[False] * n for _ in range(m)]
        queue = deque([(row, col, 0)]) # 행, 열, 총시간 초기화
        
        while queue:
            cur_row, cur_col, cur_time = queue.popleft()
                        
            # 현재 노드가 레버나 출구인 경우 체크
            if maps[cur_row][cur_col] == target:
                return cur_row, cur_col, cur_time
            
            # 인접 노드 탐색
            for i in range(4):
                new_row, new_col = cur_row + dr[i], cur_col + dc[i]
                # 유효성 검사 및 벽이 아닌지, 방문 유무 검사
                if 0 <= new_row < m and 0 <= new_col < n and maps[new_row][new_col] != 'X' and visited[new_row][new_col] == False:
                    queue.append((new_row, new_col, cur_time + 1))
                    visited[new_row][new_col] = True
            
        # 탈출 못하는 경우
        return cur_row, cur_col, -1

    # 시작 지점을 찾아 BFS 수행
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                lever_row, lever_col, time1 = bfs(i, j, 'L')
    exit_row, exit_col, time2 = bfs(lever_row, lever_col, 'E')
    
    if time1 == -1 or time2 == -1:
        return -1
    else:
        return time1 + time2
    