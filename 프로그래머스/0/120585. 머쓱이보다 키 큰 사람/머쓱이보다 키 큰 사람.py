def solution(array, height):
    
    count = 0
    for e in array:
        if e > height:
            count += 1
    
    return count