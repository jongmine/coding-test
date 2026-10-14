def solution(numbers):
    
    # 모든 숫자를 문자열로 변환
    str_nums = list(map(str, numbers))
    
    # 변환 후 내림차순 정렬
    # 최대 1000이므로 *3을 통해 자릿수를 맞춰서 정확하게 비교)
    str_nums.sort(key=lambda x: x * 3, reverse=True)
    
    # 정렬된 문자열 합친 후 return
    answer = "".join(str_nums)
    
    # 정렬했을 때 맨 앞 글자가 0이면 모든 숫자가 0이므로 문자열 '0' 반환 
    if answer[0] == '0':
        return '0'
    else:
        return answer
