# 각 종류의 의상 수들의 곱
# 의상을 입지 않는 경우도 고려해야 함
# 모든 의상을 아예 안입진 않음


def solution(clothes):
    clothes_dict = {}
    
    # 이름, 종류를 뽑아서 k(종류) : v(이름의 개수) 로 저장
    for v, k in clothes:
        clothes_dict[k] = clothes_dict.get(k, 0) + 1
        
    # 경우의 수 계산: 각 종류 개수들의 곱 -> v들의 곱의 합
    answer = 1
    for v in clothes_dict.values():
        answer *= (v + 1) # 해당 종류 자체를 아예 입지 않는 경우 고려
    
    return answer - 1 # 모든 의상을 아예 안 입는 경우 제외
