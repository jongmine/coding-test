input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


# 1. memo에 해당값이 존재하면 반환
# 2. 없는 경우 그 값으 피보나치를 통해 구한 후 memo에 저장
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


print(fibo_dynamic_programming(input, memo))