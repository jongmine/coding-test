# Q1. 쓱 최대로 할인 적용하기
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
import collections

from collections import deque


shop_prices = [30000, 2000, 1500000] # 상품의 가격
user_coupons = [20, 40]              # 쿠폰, 할인율의 단위는 % 입니다.


def get_max_discounted_price(prices, coupons):
    total_price = 0

    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    prices_queue = deque(prices)
    coupons_queue = deque(coupons)

    while prices_queue:
        if coupons_queue:
            price = prices_queue.popleft() * (100 - coupons_queue.popleft()) // 100
        else:
            price = prices_queue.popleft()

        total_price += price

    return total_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
