import heapq


def solution(scoville, K):
    # min heap 생성
    heap = []
    
    # 작은 음식부터 순회하며 음식 섞기
    for i in scoville:
        heapq.heappush(heap, i)
    
    count = 0
    while heap[0] < K: # K를 넘길 때까지 반복
        # 두 개 이상 남아있어야 함
        if len(heap) < 2:
            return -1
        # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        min_1st = heapq.heappop(heap)
        min_2nd = heapq.heappop(heap)
        mixed = min_1st + (min_2nd * 2)
        heapq.heappush(heap, mixed)
        count += 1
        
    return count
