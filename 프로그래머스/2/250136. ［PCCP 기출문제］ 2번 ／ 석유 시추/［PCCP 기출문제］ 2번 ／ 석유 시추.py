from collections import deque


def solution(land):
    
    # row, col의 개수
    m, n = len(land), len(land[0]) 
    visited = [[False] * n for _ in range(m)]
    
    # 상, 하, 좌, 우 
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 열별로 최대로 시추 가능한 석유량
    amounts_by_col = [0] * n 
    
    # 1. 수직 이동하며 석유 탐색 -> 시간 초과
    # 석유를 찾으면 해당 위치를 시작점으로 하여 BFS로 탐색하여 해당 노드에 매장된 석유량 가산 
    # 모든 열에 대해 탐색하며 위 과정 반복
#     def bfs(r, c):
#         queue = deque([[r, c]]) # 시작 노드의 r, c 좌표
        
#         # 시작 노드 초기화
#         visited[r][c] = True
#         amounts = 0 # 이 탐색으로 얻을 수 있는 석유 시추량
        
#         while queue:
#             r, c = queue.popleft()
#             amounts += 1 # 시추한 석유량 추가
#             for i in range(4):
#                 new_r, new_c = r + dr[i], c + dc[i]
                
#                 # 새로운 r, c 좌표가 유효하며 아직 시추되지 않은 영역인 경우 탐색 후보에 추가
#                 if 0 <= new_r < m and 0 <= new_c < n and not visited[new_r][new_c] and land[new_r][new_c] == 1:
#                     queue.append([new_r, new_c])
#                     visited[new_r][new_c] = True
                
#         return amounts
    

#    # 수직방향으로 모든 열에 대해 석유가 있는 좌표 탐색
#     for j in range(n):
#         # 노드 방문 여부 (열마다 초기화)
#         visited = [[False] * n for _ in range(m)]
#         for i in range(m):
#             # 석유가 존재하며 아직 시추되지 않은 노드부터 시작하여 탐색
#             if land[i][j] == 1 and visited[i][j] == False:
#                 amounts_by_col[j] += bfs(i, j)
    
    # 2. 열마다 중복 탐색을 제거하여 해당 영역이 걸치는 열의 총합 석유 시추량에 가산
    def bfs(r, c):
        queue = deque([[r, c]]) # 시작 노드의 r, c 좌표

        # 시작 노드 초기화
        visited[r][c] = True
        amounts = 0 # 이 탐색으로 얻을 수 있는 석유 시추량
        related_cols = set() # 가산 대상 열

        while queue:
            r, c = queue.popleft()
            related_cols.add(c) # 영역에 해당하는 열
            amounts += 1 # 시추한 석유량 추가
            for i in range(4):
                new_r, new_c = r + dr[i], c + dc[i]

                # 새로운 r, c 좌표가 유효하며 아직 시추되지 않은 영역인 경우 탐색 후보에 추가
                if 0 <= new_r < m and 0 <= new_c < n and not visited[new_r][new_c] and land[new_r][new_c] == 1:
                    queue.append([new_r, new_c])
                    visited[new_r][new_c] = True

        return amounts, list(related_cols)
    
    # 그래프를 순차대로 탐색하며 열별로 석유시추량 가산
    for i in range(m):
        for j in range(n):
            
            # 석유가 존재하며 아직 시추되지 않은 노드부터 시작하여 탐색
            if land[i][j] == 1 and visited[i][j] == False:
                amounts_by_area, related_cols = bfs(i, j)
            
                # 열별로 해당 영역을 가산
                for c in related_cols:
                    amounts_by_col[c] += amounts_by_area
                
    print(amounts_by_col)
    # 가장 많은 석유를 시추할 수 있는 열에 매장된 석유량 반환
    return max(amounts_by_col)
