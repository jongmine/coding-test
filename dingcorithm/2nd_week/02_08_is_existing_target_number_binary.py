finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
#     mid = len(array) // 2
#
#     if len(array) == 0:
#         return False
#
#     if array[mid] == target:
#         return True
#
#     if array[mid] < target:
#         return is_existing_target_number_binary(target, array[mid + 1:])
#
#     if array[mid] > target:
#         return is_existing_target_number_binary(target, array[:mid])
#
#     return False

    find_count = 0
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False

# 시간 복잡도
# 1번: 1 ~ N
# 2번: 1 ~ N/2
# 3번: 1 ~ N/4
# ...
# K번: 1 ~ N/2^k -> K번 탐색하면 N/2^k개가 남는다.
# N = 2^k, log2(N) = k, => O(log(N))


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)