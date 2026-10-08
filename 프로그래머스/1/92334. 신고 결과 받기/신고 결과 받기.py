def solution(id_list, report, k):
    
    # 한 번에 한 명 유저 신고 가능 (중복 허용 X)
    # k번 이상 신고 누적 시 이용 정지 후 신고한 유저에게 메일 발송
    # 각 유저별로 처리 결과 메일을 받은 횟수 배열 반환
    
    # 1. 나를 신고한 유저를 set타입 value로 저장
    hashed_ids = {id: set() for id in id_list}
    mail_counts = {id: 0 for id in id_list}
    
    for r in report:
        reporter, user = r.split(' ')
        hashed_ids[user].add(reporter)
    
    # 2. set의 원소 개수가 k 이상인 경우 정지 및 원소들에 있는 유저들에게 메일 발송
    # 중복 신고를 제외하기 위해 hashed_ids 값인 set 원소의 개수를 카운트
    for key, value in hashed_ids.items():
        if len(value) >= k:
            for reporter in value:
                mail_counts[reporter] += 1
                
    return list(mail_counts.values())
        