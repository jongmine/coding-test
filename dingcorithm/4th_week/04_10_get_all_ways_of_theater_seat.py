# Q3. 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
#
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
#
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고,
# 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.
#
# 그런데 이 극장에는 “VIP 회원”들이 있다.
# 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.
#
# 예를 들어서,
# 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.
#
# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.


# 1. 경우의 수
# [1, 2] -> [1, 2], [2, 1] -> 1
# [1, 2, 3] -> [1, 2, 3], [2, 1, 3], [1, 3, 2] -> 2
# [1, 2, 3, 4] -> [1, 2, 3, 4], [2, 1, 3, 4], [1, 3, 2, 4], [1, 2, 4, 3], [2, 1, 4, 3] -> 3
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [1, 3, 2, 4, 5], [1, 2, 4, 3, 5], [1, 2, 3, 5, 4], [2, 1, 4, 3, 5], [2, 1, 3, 5, 4], [1, 3, 2, 5, 4] -> 8
# ...
# => 피보나치 수열

# 2. 점화식
# 좌석 n개: 1, 2, 3, ..., n-2, n-1, n
# n번째 티켓을 가진 사람이 앉을 수 있는 경우의 수:
# 1. n번째:
# -> 이 상황에서는 잔여 좌석은 n-1개에 n-1명을 배치해야 함 = F(N-1)
# 2. n-1번 -> n-1번 티켓 소유자는 n번에 앉기
# ->  이 상황에서는 잔여 좌석은 n-2개에 n-2명을 배치해야 함 = F(N-2)
#
# => N명을 N개 좌석에 배치 = F(N) = F(N-1) + F(N-2)


# 4, 7은 고정석 -> 1~3, 4, 5~6, 7, 8~9 구간으로 나누어 계산
# f(3) * f(2) * f(2)

seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo



def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))