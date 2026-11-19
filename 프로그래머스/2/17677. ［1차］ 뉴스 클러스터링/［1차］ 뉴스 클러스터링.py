
# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 나눗셈이 정의되지 않으면 J(A, B) = 1로 정의
# 다중집합의 경우 원소의 중복 허용 -> 딕셔너리로 각 원소 개수 카운트
# 교집합: min,  합집합: max


def solution(str1, str2):
    
    # 1. 두 글자씩 파싱하여 다중집합 생성
    # 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버림 -> a: 97, z: 122
    str1, str2 = str1.lower(), str2.lower() # 소문자로 초기화
    set1, set2 = {}, {}
    
    word = '_' + str1[0] # 두 글자, 첫 글자 초기화
    for i in range(1, len(str1)):
        word = word[1:]
        word += str1[i]
        
        # 단어가 모두 알파벳으로 이루어져 있으면 딕셔너리 키로 등록 후 카운트 증가
        if word.isalpha():
            set1[word] = set1.get(word, 0) + 1
            
    word = '_' + str2[0] # 두 글자, 첫 글자 초기화
    for i in range(1, len(str2)):
        word = word[1:]
        word += str2[i]
        
        # 단어가 모두 알파벳으로 이루어져 있으면 딕셔너리 키로 등록 후 카운트 증가
        if word.isalpha():
            set2[word] = set2.get(word, 0) + 1
    

    # 2. 원소 개수 별로 교집합(min), 합집합(max) 계산
    intersection, union = 0, 0
    
    for e in set1:
        if e in set2:
            intersection += min(set1[e], set2[e])
            union += max(set1[e], set2[e])
        else:
            union += set1[e]
            
    for e in set2:
        if e not in set1:
            union += set2[e]
    
    # union = sum(set1.values()) + sum(set2.values()) - intersection
            
    
    # 3. 유사도 계산: 교집합/합집합 or 1
    print(set1, set2)
    print(intersection, union)
    answer = 1
    if union != 0:
        answer = intersection / union
    
    
    # 4. *65536 후 정수부만 반환
    return int(answer * 65536)
    