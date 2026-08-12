def solution(clothes):
    clothes_dict = dict()
    
    for v, k in clothes:
        if k not in clothes_dict:
            clothes_dict[k] = []
        clothes_dict[k].append(v)

    # (종류1 + 1) * (종류2 + 1) * ... - 아무 종류도 입지 않는 경우의 수
    answer = 1 # 곱셈을 위해 1로 시작
    for v in clothes_dict.values():
        answer *= len(v) + 1 # 각 의상 종류별로 곱하기 + 해당 의상을 입지 않는 경우의 수 추가

    return answer - 1 # 아무 것도 안 입는 경우의 수 제거