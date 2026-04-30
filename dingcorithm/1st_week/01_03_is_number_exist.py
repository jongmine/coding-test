# 알파벳 찾기
# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.
# [3, 5, 6, 1, 2, 4]


# 배열의 모든 요소를 순회
# O(N), Ω(1)의 시간복잡도
def is_number_exist(number, array):
    for i in array:
        if i == number:
            return True
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = False 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))

# 1. 입력값에 비례하여 얼마나 늘어날지 파악해보기
# 2. 공간 복잡도 보다는 시간 복잡도를 더 줄이기 위해 고민하기
# 3. 최악의 경우 시간ㄴ이 얼마나 소요될 지(빅오 표기법)에 대해 고민하기
