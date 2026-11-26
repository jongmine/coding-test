# 1. 1명씩 줄의 맨 뒤에 추가
# 2. 본인보다 작은 학생이 1명이라도 있다면 본인이 맨 앞으로 이동


P = int(input())
for _ in range(1, P + 1):
    test_case = list(map(int, input().split()))
    T = test_case[0]
    students = test_case[1:]
        
    line = []
    count = 0
    
    for i in range(20):
        line.append(students[i])
        
        # 현재줄에서 앞에 서있는 인원들과 비교
        for j in range(i):
            # 마지막 인원보다 큰 인원이 있으면 맨 앞에 추가
            if line[i] < line[j]:
                line.insert(j, line.pop())
                count += i - j
                break
            
    print(T, count)
