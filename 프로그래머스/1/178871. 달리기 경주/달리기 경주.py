def solution(players, callings):
    
    # 1. 리스트로 풀기 -> 시간 초과
    # for c in callings:
    #     front = players.index(c)
    #     back = front - 1
    #     # 불린 선수 이름과 그 이전 인덱스 선수와 순서 바꾸기
    #     players[front], players[back] = players[back], players[front]
    
    # 2. 해시로 풀기
    rank = {} # 선수 이름 : 순위
    for i, p in enumerate(players):
        rank[p] = i
    
    for c in callings:
        front_i = rank[c]
        front = players[front_i]
        back_i = front_i - 1
        back = players[back_i]
        
        # 불린 선수 이름과 그 이전 인덱스 선수와 순서 바꾸기
        players[front_i], players[back_i] = back, front
        rank[front], rank[back] = back_i, front_i
    
    return players
    