def solution(money):
    answer = []
    
    q = int(money / 5500)
    r = money  % 5500
    answer.append(q)   
    answer.append(r)
    
    return answer