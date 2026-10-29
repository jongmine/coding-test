def solution(points, routes):
    
    # 이동 기록을 추적하기 위한 딕셔너리 
    # k: 시간, 현재좌표(리스트는 키가 될 수 없음 유의) / v: 방문횟수
    history = {}
    # 노드 번호 1부터 시작
    nodes = [None] + points
        
    # 최단 경로로 이동
    for r in routes:
        start = nodes[r[0]]
        current_r, current_c = start[0], start[1]
        time = 0
        
        # 시작 노드부터 카운트 증가
        if (time, current_r, current_c) not in history:
            history[(time, current_r, current_c)] = 0
        history[(time, current_r, current_c)] += 1
        
        # 순서대로 목적지 경유
        for i in range(1, len(r)):
            dest = nodes[r[i]]
            dest_r, dest_c = dest[0], dest[1]
        
            # r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저
            # 상하 이동
            while current_r != dest_r:
                if current_r < dest_r:
                    current_r += 1
                else:
                    current_r -= 1
                time += 1

                # 이동 기록
                if (time, current_r, current_c) not in history:
                    history[(time, current_r, current_c)] = 0
                history[(time, current_r, current_c)] += 1

            # 좌우 이동
            while current_c != dest_c:
                if current_c < dest_c:
                    current_c += 1
                else:
                    current_c -= 1
                time += 1

                # 이동 기록
                if (time, current_r, current_c) not in history:
                    history[(time, current_r, current_c)] = 0
                history[(time, current_r, current_c)] += 1

    # 특정 시점의 노드의 방문 횟수가 2 이상이면 충돌로 판정
    counts = 0
    for count in history.values():
        if count >= 2:
            counts += 1

    return counts
