from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque((i, p) for i, p in enumerate(priorities)) # (인덱스, 우선순위)
    
    while queue:
        current_i, current_p = queue.popleft() # 현재 꺼낸 프로세스의 초기 인덱스와 우선순위
        
        if any(current_p < process[1] for process in queue): # 꺼낸 프로세스보다 우선순위 높은 프로세스가 queue에 있는지 확인
            queue.append((current_i, current_p)) # 뒤로 보내기
        else:
            answer += 1 # 실행 사이클 증가
            if current_i == location:
                return answer
