import re # 정규표현식 모듈 사용


def solution(message, spoiler_ranges):
    spoiler_words = [] # 왼쪽부터 찾아야 하므로 list 사용
    normal_words = set() # 편하게 중복 제거하기 위해 set 사용
    
    # 1. 스포 방지 단어 찾기
    # 스포 방지 단어 판별: 단어중 한글자라도 스포 방지 구간에 속할 때 -> 두 조건 모두 만족
#     # 1. 직접 단어 찾기
#     # - 단어 시작이 스포방지구간 끝보다 앞에 있어야 함: w_start <= s_end
#     # - 단어 끝이 스포방지구간 시작보다 뒤에 있어야 함: w_end >= s_start
#     # 단어 시작/끝 인덱스
#     w_start, w_end = None, None
#     for i, c in enumerate(message):
#         # 단어 시작 인덱스 찾기
#         # 1-문자가 공백이 아니며 단어가 시작하지 않은 경우
#         if c != " " and w_start is None:
#             w_start = i
        
#         # 단어 끝 인덱스 찾기
#         # 단어 집합에 추가 및 스포 방지 단어 식별
#         # 2-마지막 문자가 공백이며 단어가 이미 시작한 경우
#         elif c == " " and w_start is not None:
#             w_end = i - 1 # 공백 직전까지
#             word = message[w_start:i]
            
#             # 판별한 단어와 스포 방지 구간을 비교하여 스포 방지 단어인지 판별
#             is_spoiler_word = False
#             for s_start, s_end in spoiler_ranges:
#                 if (w_start <= s_end) and (w_end >= s_start):
#                     is_spoiler_word = True
#                     break
            
#             if is_spoiler_word is True:
#                 spoiler_words.append(word)
#             else:
#                 normal_words.add(word)
                
#             w_start = None # 다음 단어를 위한 초기화
        
#     # 3-마지막 문자가 문자이며 단어가 이미 시작한 경우
#     if c != " " and w_start is not None:
#         w_end = len(message) - 1
#         word = message[w_start:]

#         # 판별한 단어와 스포 방지 구간을 비교하여 스포 방지 단어인지 판별
#         is_spoiler_word = False
#         for s_start, s_end in spoiler_ranges:
#             if (w_start <= s_end) and (w_end >= s_start):
#                 is_spoiler_word = True
#                 break

#         if is_spoiler_word is True:
#             spoiler_words.append(word)
#         else:
#             normal_words.add(word)

#         w_start = None # 다음 단어를 위한 초기화

    # 2. 정규표현식으로 단어와 인덱스를 통째로 추출하기
    for match in re.finditer(r'\S+', message):
        word = match.group()    # 단어 추출
        w_start = match.start()
        w_end = match.end() - 1 # match.end()는 단어 바로 다음 위치 반환하므로 - 1
        
        # 판별한 단어와 스포 방지 구간을 비교하여 스포 방지 단어인지 판별
        is_spoiler_word = False
        for s_start, s_end in spoiler_ranges:
            if (w_start <= s_end) and (w_end >= s_start):
                is_spoiler_word = True
                break
                
        if is_spoiler_word:
            spoiler_words.append(word)
        else:
            normal_words.add(word)            
        
            
    # 2. 중요한 단어 찾기
    # 일반 단어에 이미 노출되지 않았고 이미 찾은 스포 방지 단어와 중복 X
    important_words = []
    for w in spoiler_words:
        if w not in important_words and w not in normal_words:
            important_words.append(w)
            
    return len(important_words)
