from collections import deque


def solution(arr):
    queue = deque(arr)
    answer = []
    last_inserted = None
    
    while queue:
        current = queue.popleft()
        if current != last_inserted:
            answer.append(current)
            last_inserted = current
        
    return answer