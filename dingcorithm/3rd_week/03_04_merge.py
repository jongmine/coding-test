array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!

    result = []

    index_1 = 0
    index_2 = 0

    # 인덱스 접근을 먼저 하고 배열이 끝났는지 검사하는 것은 위험한 방식
    # while len(result) < len(array1) + len(array2):
    #     if array1[index_1] < array2[index_2]:
    #         result.append(array1[index_1])
    #         index_1 += 1
    #     else:
    #         result.append(array2[index_2])
    #         index_2 += 1
    #
    #     if index_1 >= len(array1):
    #         result.extend(array2[index_2:])
    #     elif index_2 >= len(array2):
    #         result.extend(array1[index_1:])

    # 인덱스 조건 검사를 먼저 수행
    while index_1 < len(array1) and index_2 < len(array2):
        if array1[index_1] < array2[index_2]:
            result.append(array1[index_1])
            index_1 += 1
        else:
            result.append(array2[index_2])
            index_2 += 1

    # 넣지 못한 배열들 넣기
    while index_1 < len(array1):
        result.append(array1[index_1])
        index_1 += 1

    while index_2 < len(array2):
        result.append(array2[index_2])
        index_2 += 1

    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))