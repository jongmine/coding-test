def solution(survey, choices):
    
    # RT CF JM AN dict
    scores = {'R' : 0, 'T': 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    # s를 슬라이싱해서 문자 구한 후 해당 유형에 점수 가산
    # 중앙값 4 기준으로 1-3점 가산
    for s, c in zip(survey, choices):
        if c < 4:
            scores[s[0]] += -c + 4
        elif c > 4:
            scores[s[1]] += c - 4
        else:
            pass
        
    # 알파벳순으로 유형 초기화
    answer = ['R', 'C', 'J', 'A']
    
    # 두번째 유형이 첫번째 유형보다 점수가 높은 경우에만 변경
    if scores['R'] < scores['T']:
        answer[0] = 'T'
    if scores['C'] < scores['F']:
        answer[1] = 'F'
    if scores['J'] < scores['M']:
        answer[2] = 'M'
    if scores['A'] < scores['N']:
        answer[3] = 'N'
            
    return ''.join(answer)