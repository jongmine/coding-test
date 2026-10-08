def solution(video_len, pos, op_start, op_end, commands):
    
    # "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동
    # "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동
    # 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동
    
    def make_seconds(time_str):
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)
    
    
    def make_minutes_and_seconds(seconds):
        m = seconds // 60
        s = seconds % 60
        return str(m).zfill(2) + ':' + str(s).zfill(2)
    
    
    # 모든 시간을 초로 환산
    video_len_s = make_seconds(video_len)
    pos_s = make_seconds(pos)
    op_start_s = make_seconds(op_start)
    op_end_s = make_seconds(op_end)
    pos_s = make_seconds(pos)
    time = pos_s
    
    # 오프닝 만나면 자동 건너뛰기
    if op_start_s <= time <= op_end_s:
        time = op_end_s
    
    # 모든 commands를 마칠 때까지 시간 진행
    for c in commands:
        print('명령 전', make_minutes_and_seconds(time))
            
        if c == 'prev':
            time = max(time - 10, 0)
        elif c == 'next':
            time = min(time + 10, video_len_s)
        print('명령 후', make_minutes_and_seconds(time))
                
        # 오프닝 만나면 자동 건너뛰기
        if op_start_s <= time <= op_end_s:
            time = op_end_s

        print('오프닝 유무 검증 후', make_minutes_and_seconds(time))


    return make_minutes_and_seconds(time)
