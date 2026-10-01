def solution(today, terms, privacies):
    answer = []
    
    # 약관별 유효기간(일)
    policy_dates = {}
    for i in terms:
        current_term, valid_month = i.split(' ')
        policy_dates[current_term] = int(valid_month) * 28    
    
    # 모든 달은 28일까지 있다고 가정: 년/월을 일로 변환
    t_year, t_month, t_day = today.split('.')
    t_days = int(t_year) * 12 * 28 + int(t_month) * 28 + int(t_day)
       
    # 각 동의 날짜를 일로 변환
    for i, item in enumerate(privacies):
        p_date, p_term = item.split(' ')
        p_year, p_month, p_day = p_date.split('.')
        p_days = int(p_year) * 12 * 28 + int(p_month) * 28 + int(p_day)
        
        # 동의 날짜 + 약관별 유효일 <= 현재 날짜인 경우 파기
        if p_days + policy_dates[p_term] <= t_days:
            answer.append(i + 1)
        
    return answer
