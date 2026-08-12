def solution(phone_book):
    phone_set = set(phone_book)
    
    for p in phone_book:
        for i in range(1, len(p)):
            prefix = p[:i]
            if prefix in phone_set:
                return False
            
    return True