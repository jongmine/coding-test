def solution(num_list):
    
    odd_count = 0
    even_count = 0
    
    for e in num_list:
        if e % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return [even_count, odd_count]