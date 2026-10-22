def solution(diffs, times, limit):
    
    low = 1
    high = max(diffs)
    
    # 이진 탐색으로 모든 문제를 limit 안에 풀 수 있는 최적의 level을 찾을 때까지 반복
    while low <= high:
        mid = (low + high) // 2 # 검증할 level
        
        solve_time = times[0] # 퍼즐 풀이 시간
        is_exceed = False # limit 초과 유무 플래그
        
        # diff를 순회하며 solve_time 계산
        for i in range(1, len(diffs)):
            time_cur = times[i]
            time_prev = times[i - 1]
            diff = diffs[i]
             
            # 1. level보다 난이도가 낮거나 같은 경우
            if diff <= mid:
                solve_time += time_cur
            # 2. level보다 난이도가 높은 경우
            else:
                solve_time += (time_prev + time_cur) * (diff - mid) + time_cur
                
            # limit을 초과한 경우 실패 처리
            if solve_time > limit:
                is_exceed = True
                break
                
        # 실패한 경우 level을 올리고 성공한 경우 level 낮추기
        if is_exceed:
            low = mid + 1
        else:
            answer = mid
            high = mid - 1
            
    return answer
