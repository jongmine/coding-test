def solution(friends, gifts):
    # 예상되는 받을 선물 개수
    expected_gifts = {name: 0 for name in friends}
    
    # 선물 지수
    gift_index = {name: 0 for name in friends}
    
    # 사람간 관계 초기화: {이름: {이름: 선물지수, ...}, ...}
    graph = {name: {} for name in friends}
    for p1 in friends:
        for p2 in friends:
            if p1 != p2:
                graph[p1][p2] = 0 
    
    # 선물 주고 받은 이력, 선물 지수 정리
    for names in gifts:
        p1, p2 = names.split()
        graph[p1][p2] += 1
        gift_index[p1] += 1
        gift_index[p2] -= 1
        
    # 다음달 받을 선물 개수 계산
    n = len(friends)
    for i in range(n):
        for j in range(i + 1, n): # 중복 제거를 위해 i + n부터
            p1, p2 = friends[i], friends[j]
            p1_to_p2 = graph[p1][p2]
            p2_to_p1 = graph[p2][p1]
            
            # 1. 선물 기록 기반 받을 선물 개수 계산
            if p1_to_p2 > p2_to_p1:
                expected_gifts[p1] += 1
            elif p1_to_p2 < p2_to_p1:
                expected_gifts[p2] += 1
            
            # 2. 주고받은 수가 같다면 선물 지수 기반 받을 선물 개수 계산
            else:
                if gift_index[p1] > gift_index[p2]:
                    expected_gifts[p1] += 1
                elif gift_index[p1] < gift_index[p2]:
                    expected_gifts[p2] += 1
            
    return max(expected_gifts.values())