import heapq


def solution(operations):
    
    answer = [0, 0]
    
    # 최소, 최대 힙
    min_heap = []
    max_heap = []
    memo = set() # 두 힙 동기화를 위한 메모: 연산의 idx(순서)가 유효한지 저장
    
    for i, op in enumerate(operations):
        instruction, number = op.split()
        number = int(number)
        
        if instruction == 'I': # I 숫자: 숫자 삽입
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
            memo.add(i)
            
        elif instruction == 'D':
            if number == 1: # D 1: 최댓값 삭제
                # memo에 유효하지 않은 값이 있다면 삭제처리
                while max_heap and max_heap[0][1] not in memo:
                    heapq.heappop(max_heap)
                
                # 힙에서 최종 최댓값 찾은 후 memo 무효화
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    memo.remove(idx)
                
            elif number == -1: # D -1: 최솟값 삭제
                # memo에 유효하지 않은 값이 있다면 삭제처리
                while min_heap and min_heap[0][1] not in memo:
                    heapq.heappop(min_heap)
                
                # 힙에서 최종 최솟값 찾은 후 memo 무효화
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    memo.remove(idx)
                    
    # memo에 유효하지 않은 값이 있다면 삭제처리
    while max_heap and max_heap[0][1] not in memo:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0][1] not in memo:
        heapq.heappop(min_heap)
    
    if min_heap and max_heap:
        answer[0] = -max_heap[0][0]
        answer[1] = min_heap[0][0]
    
    return answer
    