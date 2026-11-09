# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.


from collections import deque


c = 11
b = 2


def catch_me(cony_loc, brown_loc):

    time = 0
    max_length = 200_000

    # 모든 경우의 수를 봐야함 -> BFS, DFS
    # 시간은 선형(규칙적)이라 리스트를 사용해도 되지만, 위치가 마구잡이로(불규칙적) 움직임 -> 딕셔너리 사용
    # N초에 위치할 수 있는 경우의 수 -> {위치:최근방문시간 N}
    # e.g.: {10:3}
    # visited = {}
    visited = {brown_loc: 0}
    queue = deque([(brown_loc, time)])

    while cony_loc <= max_length: # 이동할 수 있는 위치
        cony_loc += time

        # 코니의 시간과 위치가 브라운의 시간과 위치가 동일하면 현재시간 반환
        # visited [위치]->{시간:값} 에서 cony_loc 위치에 해당하는 딕셔너리에 time이 키로 존재하면 해당 위치에 브라운이 time에 위치한다는 의미
        if time == visited.get(cony_loc):
            return time

        for i in range(0, len(queue)): # while 대신 for? 현재시간에 해당하는 경우의 수만 고려하기 위함

            # 현재 브라운의 위치, 시간
            current_loc, current_time = queue.popleft()

            # 유효성 검사 후 브라운 이동
            new_time = current_time + 1

            # 같은 위치에 같은 시간으로 이미 방문한 적이 없을때만 큐에 적재해서 시간초과 방지
            new_loc = current_loc + 1
            if new_loc <= max_length and visited.get(new_loc) != new_time: # 1. + 1 이동
                visited[new_loc] = new_time
                queue.append((new_loc, new_time))

            new_loc = current_loc - 1
            if 0 <= new_loc and visited.get(new_loc) != new_time: # 2. - 1 이동
                visited[new_loc] = new_time
                queue.append((new_loc, new_time))

            new_loc = current_loc * 2
            if new_loc <= max_length and visited.get(new_loc) != new_time: # 3. * 2 이동
                visited[new_loc] = new_time
                queue.append((new_loc, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
print("정답 = 0 / 현재 풀이 값 = ", catch_me(10, 10))
print("정답 = 0 / 현재 풀이 값 = ", catch_me(200000, 200000))
print("정답 = -1 / 현재 풀이 값 = ", catch_me(200000, 0))
print("정답 = 5 / 현재 풀이 값 = ", catch_me(1, 0))
print("정답 = 1 / 현재 풀이 값 = ", catch_me(0, 1))


# 오답: 시간 초과 -> 너무 많은 경우의 수를 고려 못함
# def catch_me(cony_loc, brown_loc):
#     # 브라운이 코니를 잡거나 코니가 먼저 끝까지 달아나면 종료
#     # 위치: 0 <= x <= 200,000
#     # 코니 이동 속도는 초마다 +1씩 증가 -> 우측 방향으로 이동
#     # 브라운은 -1, +1, *2로 이동 가능
#
#     max_time = 200_000
#
#     # 0초에 둘의 위치가 같은 경우
#     if cony_loc == brown_loc:
#         return 0
#
#
#     # 코니의 시간별 위치를 미리 계산 후 브라운이 해당 시간에 코니 위치에 도달하는 최소 시간 찾기 -> 완전 탐색
#     cony_loc_history = []
#     cony_time = 0
#     for t in range(1, max_time + 1):
#         cony_loc_history.append(cony_loc)
#         cony_time += 1
#         cony_loc += cony_time
#
#     # 브라운 이동
#     brown_time = 0  # 소요시간
#     queue = deque([(brown_time, brown_loc)])
#
#     while queue:
#         current_time, current_loc = queue.popleft()
#
#         # 브라운이 이동한 위치가 코니를 잡을 수 있다면 반환, 아니라면 큐에 추가
#         # 1. -1 이동
#         if cony_loc_history[current_time] == current_loc - 1:
#             return brown_time
#         else:
#             queue.append((current_time + 1, current_loc - 1))
#
#         # 2. +1 이동
#         if cony_loc_history[current_time] == current_loc + 1:
#             return brown_time
#         else:
#             queue.append((current_time + 1, current_loc + 1))
#
#         # 3. *2 이동
#         if brown_loc * 2 <= max_time and cony_loc_history[current_time] == current_loc * 2:
#             return brown_time
#         else:
#             queue.append((current_time + 1, brown_loc * 2))