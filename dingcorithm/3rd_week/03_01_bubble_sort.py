# 버블 정렬은 첫 번째 자료와 두 번째 자료를, 두 번째 자료와 세 번째 자료를, 세 번째와 네 번째를, …
# 이런 식으로 (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬하는 방식입니다!
# 작은 숫자, 큰 숫자 순서로 있으면 내버려두고 큰 숫자, 작은 숫자 순서로 있으면 둘의 위치를 변경하시면 됩니다!

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # O(N^2)
    for i in  range(len(array) - 1): # O(N)
        for j in range(len(array) - 1 - i): # O(N)
            print(i, j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))