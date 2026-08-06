import math
from collections import deque


def solution(progresses, speeds):
    answer = [] # stack
    
    p_queue = deque(progresses)
    s_queue = deque(speeds)
    days = deque()
    
    while p_queue:
        # 매일 속도만큼 작업 진행
        for i in range(len(p_queue)):
            p_queue[i] += s_queue[i]
        
        # 선행 작업이 완료되었을 때 배포할 작업 개수 결정
        count = 0
        while p_queue and p_queue[0] >= 100:
            p_queue.popleft()
            s_queue.popleft()
            count += 1
            
        if count > 0:
            answer.append(count)
            
    return answer