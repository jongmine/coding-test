def solution(participant, completion):    
    answer = {}
    
    for p in participant:
        answer[p] = answer.get(p, 0) + 1 # 있으면 p, 없으면 0을 가져와 +1
        
    for c in completion:
        answer[c] -= 1
    
    for key in answer:
        if answer[key] > 0:
            return key
