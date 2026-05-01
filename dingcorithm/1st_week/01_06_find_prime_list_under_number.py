# 6. 소수 구하기
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

input = 20


# 1. 비교할 수보다 작은 소수들끼리만 비교하기
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for i in range(2, number + 1):
#         # i보다 작은 소수들에 대해서만 비교
#         for j in prime_list:
#             if i % j == 0:
#                 break
#         else:
#             prime_list.append(i)
#
#     return prime_list

# 2. N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
def find_prime_list_under_number(number):
    prime_list = []

    for i in range(2, number + 1):
        for j in prime_list:
            if j * j <= i and i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
