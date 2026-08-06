from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge_queue = deque([0] * bridge_length)

    time = 0
    bridge_weight = 0

    while truck_queue or bridge_queue:
        # 다리에서 트럭 1대 나가기
        if len(bridge_queue) > 0:
            bridge_weight -= bridge_queue.popleft()

        # 새 트럭 다리 진입
        # 다리를 통과하기 위해 대기하는 트럭이 남아 있을 때, 현재 다리 무게 + 진입하려는 트럭의 무게가 weight 이하인 경우
        if truck_queue and bridge_weight + truck_queue[0] <= weight:
            new_truck = truck_queue.popleft()
            bridge_weight += new_truck
            bridge_queue.append(new_truck)
        # 새 트럭이 다리 진입 못하는 경우, 간격 유지를 위해 0kg 삽입
        if len(bridge_queue) < bridge_length and truck_queue:
            bridge_queue.append(0)
        time += 1

    answer = time
    return answer
