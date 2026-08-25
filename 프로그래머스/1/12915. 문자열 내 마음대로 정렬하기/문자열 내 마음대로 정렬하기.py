def solution(strings, n):
    new_string = []
    answer = []
    
    # 인덱수 N번째 기준으로 정렬하는거라 좀 편법써서
    
    for s in strings:
        new_string.append(s[n] + s)
        #                   여기 -> 알파벳을 맨 앞에 넣고, 그리고 뒤에는 기존 문자열 넣어서 새 리스트 만들고
        
    new_string.sort() # 여기서 정렬하면 해당 인덱스번째에서 정렬이되겠죠?
    
    for s in new_string:
        answer.append(s[1:]) # 맨앞 붙였던거 제거 후 리턴
    
    return answer