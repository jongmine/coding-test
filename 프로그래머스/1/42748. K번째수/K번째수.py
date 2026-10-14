def solution(array, commands):
    
    answer = []
    
    for i, j, k in commands:

        # array를 i-1 ~ j번째 값 자르기
        sliced = array[i-1:j]

        # 자른 array 정렬
        sliced.sort()

        # array의 k-1번째 수
        answer.append(sliced[k-1])
    
    return answer
    