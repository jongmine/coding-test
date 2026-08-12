def solution(phone_book):
    phone_hash = dict()
        
    for p in phone_book:
        phone_hash[p] = True
    for p in phone_book:        
        for i in range(1, len(p)):
            prefix = p[:i]
            if prefix in phone_hash:
                return False
            
    return True