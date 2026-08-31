def solution(numbers, target):
    answer = 0
    
#     # 1. 재귀 함수로 DFS 구현
#     def dfs(index, current_sum):
#         if index == len(numbers):
#             if current_sum == target: # 일치하면 경우의 수 반환
#                 return 1
#             else:
#                 return 0
            
#         plus = dfs(index + 1, current_sum + numbers[index])  # 더하는 경우의 수
#         minus = dfs(index + 1, current_sum - numbers[index]) # 빼는 경우의 수
        
#         return plus + minus
    
#     start_index = 0
#     current_sum = 0
#     answer = dfs(start_index, current_sum)
    
    # 2. Stack으로 DFS 구현
    stack = [(0, 0)] # index, 현재 총합
    while stack:
        index, current_sum = stack.pop()
        
        # 모든 숫자들을 합했다면 검사
        if index == len(numbers): # 모든 숫자를 탐색했는지
            if current_sum == target: # 일치하면 개수 추가
                answer += 1
            continue # 마지막 인덱스면 노드를 더 탐색하지 않고 스킵
            
        stack.append((index + 1, current_sum + numbers[index]))  # 다음 숫자를 +
        stack.append((index + 1, current_sum - numbers[index]))  # 다음 숫자를 -
        
        
    return answer

        
# DFS
#              +4              /               -4
#      +1      /       -1            +1        /        -1
#    +2/-2           +2/-2         +2/-2              +2/-2
# +1/-1 +1/-1     +1/-1 +1/-1   +1/-1 +1/-1         +1/-1 +1/-1
# ...    
