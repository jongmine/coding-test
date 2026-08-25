from collections import deque


def solution(s):
    s_stack = []
    s_queue = deque(s)
    
    while s_queue:
        char = s_queue.popleft()
        
        if char == '(':
            s_stack.append(char)            
        elif char == ')':
            if not s_stack:
                return False
            s_stack.pop()
            
    if s_stack:
        return False
    else:
        return True
