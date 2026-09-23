# 최대공약수
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수
def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)


def solution(signals): 
    # 각 신호등 [G, Y, R]
    # 모든 신호등이 노란불이 되는 가장 빠른 시각?
    
    # 1. 모든 신호등 주기의 최소공배수
    signal_lcm = sum(signals[0])
    for i in range(1, len(signals)):
        cycle_time = sum(signals[i])
        signal_lcm = get_lcm(signal_lcm, cycle_time)
    
    # 2. 0초부터 최소공배수초 동안 판별
    for t in range(0, signal_lcm):
        all_yellow = True
        
        # t초 시점에 모든 신호등이 노란불인지 확인
        for i in range(len(signals)):
            G, Y, R = signals[i]
            cycle = G + Y + R
            r = t % cycle # 주기로 나눈 나머지
            
            # 현재 r이 노란불인 경우
            if G < r <= G + Y:
                continue
            else:
                all_yellow = False
                break

        if all_yellow:
            return t
            
    return -1
