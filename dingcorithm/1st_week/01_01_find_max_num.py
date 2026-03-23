# 최댓값 찾기
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
# [3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 43, 5, 6, 1, 2, 4]

def find_max_num(array):
# 1. 하나의 원소를 다른 원소들과 비교하여 최대값인지 분석하는 방법
#     for number in array:
#         is_max_num = True
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False
#         if is_max_num:
#             return number

# 2. 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법
#     max_number = array[0]
#     for number in array:
#         if number > max_number:
#             max_number = number
#     return max_number

# 나의 풀이
    max_num = 0
    for i in array:
        if i > max_num:
            max_num = i
    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))