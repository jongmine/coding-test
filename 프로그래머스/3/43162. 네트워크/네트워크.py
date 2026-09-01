def solution(n, computers):
    answer = 0              # 처음 방문하는 노드의 개수가 네트워크 개수
    visited = [False] * n   # 각 노드의 방문 기록
    
    def dfs(root_node):
        stack = [root_node]
        
        while stack:
            node = stack.pop()
            
            if visited[node] == False:
                visited[node] = True # 현재 노드 방문 체크
                
            for next_node in range(n):
                if computers[node][next_node] == 1 and not visited[next_node]: # 존재하면 그 노드로부터 다시 재귀적으로 DFS 탐색
                    stack.append(next_node)
                        
    for i in range(n): # 모든 노드로부터 출발하여 탐색
        if not visited[i]: # 방문 X == 새 네트워크 카운트
            answer += 1
            dfs(i)
            
    return answer

#    0 1 2
# 0  1 1 0
# 1  1 1 1
# 2  0 1 1
# 0 - 1 - 2
