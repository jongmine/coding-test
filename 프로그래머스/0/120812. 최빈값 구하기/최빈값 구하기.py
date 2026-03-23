def solution(array):
	count_array = [0] * (max(array) + 1) # 숫자 출연 횟수를 셀 리스트

	for i in array:
		count_array[i] += 1

	max_count = 0 # 최빈값의 개수
	for i in count_array:
		if i == max(count_array):
			max_count += 1
    
	if max_count > 1: # 최빈값이 2개 이상이면 -1을 리턴
		return -1
	else: # 최빈값이 1개이면 해당 숫자를 리턴
		return count_array.index(max(count_array))