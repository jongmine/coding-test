from collections import deque


def solution(maps):    
    queue = deque([(0, 0, 1)]) # (노드의 x좌표, 노드의 y좌표, 이동횟수)
    visited = set()
    n, m = len(maps), len(maps[0]) # row, col의 개수
        
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 출발 지점만 방문 처리
    visited.add((0, 0))
    while queue:
        # 1. 현재 노드가 상대팀 진영인지 확인
        row, col, distance = queue.popleft()
        
        # 현재 노드가 상대팀 진영이면 거리를 반환 (BFS 이므로 현재 접근 상태가 최단거리)
        if row == n - 1 and col == m - 1:
            return distance

        
        # 2. 상하좌우 탐색 후 접근할 수 있는 노드가 있다면 큐에 추가
        for i in range(4):
            # 새로 탐색할 노드의 인덱스
            new_row = row + dr[i] 
            new_col = col + dc[i]
            
            # 인덱스 유효성 검사, 방문하지 않은 노드인지 검사
            if 0 <= new_row < n and 0 <= new_col < m and (new_row, new_col) not in visited:
                # 탐색가능 하다면 새 탐색 후보로 보고 위해 큐에 추가
                if maps[new_row][new_col] == 1:
                    queue.append((new_row, new_col, distance + 1))
                    visited.add((new_row, new_col)) # 큐에 추가하면서 방문 체크! (BFS에서는 큐에서 꺼낼 때 체크하면 중복으로 큐에 삽입될 가능성이 있음)
                    
    # 3. 모든 노드를 순회했는데도 상대팀 진영에 도달하지 못하면 -1 반환
    return -1

# [1,0,1,1,1],
# [1,0,1,0,1],
# [1,0,1,1,1],
# [1,1,1,0,0],
# [0,0,0,0,1]
