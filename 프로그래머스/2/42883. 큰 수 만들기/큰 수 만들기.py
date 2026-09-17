def solution(number, k):
    # 스택을 활용하여 큰 수 찾기
    stack = []
    
    # 문자열 앞부분부터 순회 -> 앞부분이 커야 큰 수기 때문
    # k는 소거 횟수, k가 다 소거되면 뒷부분에 큰 숫자가 나오더라도 가장 큰 수임이 보장됨
    for num in number:
        # stack의 top(현재 숫자문자열 맨뒷자리)과 그 다음 숫자 비교
        while stack and stack[-1] < num and k > 0:
            # 다음 숫자가 더 크면 현재 숫자문자열 맨뒷자리 빼기
            stack.pop()
            k -= 1 # 횟수 차감
        
        # 소거와 관계없이 다음 숫자 넣기
        stack.append(num)
        
    # 소거 횟수를 모두 소진하지 못한 경우, 맨 k개 뒷자리 제거
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)
    
    
    
    return answer