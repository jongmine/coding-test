input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 이 부분을 채워보세요!

    n = len(array)

    # for i in range(n - 1):
    #     for j in range(i + 1, 0, -1):
    #         if array[j] < array[j - 1]:
    #             array[j], array[j - 1] = array[j - 1], array[j]

    # 인덱스 i - j: 시작점 i에서 왼쪽으로 이동

    # O(N^2), 최선의 경우 Ω(N) -> 부분적으로 잘 정렬되어 있다면 더 좋은 성능
    for i in range(1, n): # O(N)
        for j in range(i): # O(N)
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else: # 이미 앞이 정렬되어 있으므로 비교 중지
                break

    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))