from collections import deque


def solution(prices):
    answer = []
    prices_queue = deque(prices)
    
    
    while prices_queue:
        not_fall_periods = 0
        current = prices_queue.popleft()
        
        for next in prices_queue:
            not_fall_periods += 1
            if current > next:
                break
                
        answer.append(not_fall_periods)   
    
    return answer
