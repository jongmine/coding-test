from collections import deque


def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    goal_q = deque(goal)
    
    # 두 카드 뭉치에서 모두 꺼내서 goal을 완성할 수 있는지 확인
    while goal_q:
        word = goal_q.popleft()
        
        if len(q1) > 0 and q1[0] == word:
            q1.popleft()
        elif len(q2) > 0 and q2[0] == word:
            q2.popleft()
        else:
            return 'No'
        
    return 'Yes'
    