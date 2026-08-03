array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


# MergeSort(0, N) = Merge(MergeSort(0, M), MergeSort(M, N))
def merge_sort(array): # O(NlogN)
    if len(array) <= 1:
        return array

    # mid = (0 + N) // 2
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array) # O(logN): N → N/2 + N/2 → N/4 + N/4 + N/4 + N/4 → ...로 함수가 logN번 호출


def merge(array1, array2): # O(N) = O(N/2) + O(N/2): 호출되는 함수의 연산량
    result = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(array1) and index_2 < len(array2):
        if array1[index_1] < array2[index_2]:
            result.append(array1[index_1])
            index_1 += 1
        else:
            result.append(array2[index_2])
            index_2 += 1

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