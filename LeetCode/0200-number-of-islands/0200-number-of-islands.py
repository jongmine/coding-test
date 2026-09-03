from collections import deque


# 연결된 노드의 집합(그래프)의 개수를 구하기
# 육지 타입이 숫자가 아닌 문자열 '1'임에 유의
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 섬의 개수
        count = 0

        # BFS 세팅
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        # 상, 하, 좌, 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)]) # row, col
            visited[start_row][start_col] = True # 첫 노드 방문 체크
            
            while queue:
                row, col = queue.popleft() # 현재 노드

                # 인접 노드들 탐색 (상, 하, 좌, 우 방향으로 탐색)
                for i in range(4):
                    new_row = row + dr[i]
                    new_col = col + dc[i]

                    # 인덱스 유효성 검사, 이미 방문한 노드인지 검사
                    if 0 <= new_row < m and 0 <= new_col < n and visited[new_row][new_col] == False:
                        if grid[new_row][new_col] == '1': # 육지인지(존재하는 노드인지) 검사
                            queue.append((new_row,new_col))
                            visited[new_row][new_col] = True
        
        # 모든 grid를 순회하며 방문하지 않은 노드를 발견하면 BFS 실행 및 섬의 개수 카운트
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False: # 방문하지 않은 육지인 경우 탐색
                    bfs(i, j)
                    count += 1
        
        return count
