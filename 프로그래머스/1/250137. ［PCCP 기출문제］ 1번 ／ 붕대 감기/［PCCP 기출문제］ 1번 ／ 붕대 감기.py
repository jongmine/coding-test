from collections import deque


def solution(bandage, health, attacks):
    
    # t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복
    # t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
    # 기술을 쓰는 도중 공격을 당하면 기술 취소, 회복 중단
    # 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용하며, 연속 성공 시간이 0으로 초기화
    # 캐릭터가 끝까지 생존할 수 있는지?
    
    # bandage: 시전 시간, 초당 회복량, 추가 회복량
    # health: 최대 체력
    # attacks[i]: 공격 시간, 피해량
    
    
    attacks_q = deque(attacks)
    remain_health = health # 남은 체력
    time = 0 # 현재 시간
    continuous_time = 0 # 연속 성공 시간
    
    # 반복문으로 시간 진행 (모든 공격이 끝날 때까지)
    while attacks_q:
        
        # 공격을 받는다면 회복 중단 및 체력 감소
        if attacks_q[0][0] == time:
            damage = attacks_q.popleft()[1]
            remain_health -= damage
            # 연속 성공시간 초기화
            continuous_time = 0
        
            # 체력이 0 이하면 -1 반환
            if remain_health <= 0:
                return -1
        
        # 공격을 받지 않는다면 붕대 감기 사용 (health 이하까지 체력 회복)
        else:
            continuous_time += 1
            remain_health = remain_health + bandage[1] if remain_health < health else health
            # 연속 회복 달성 시 추가 체력 회복
            if continuous_time == bandage[0]:
                remain_health = remain_health + bandage[2] if remain_health < health else health
                continuous_time = 0

        time += 1
    
    return remain_health
    