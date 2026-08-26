def solution(genres, plays):
    answer = []
    genre_total_play = {} # 장르별 총 재생횟수 (장르: total_N)
    genre_index_play = {} # 장르별 인덱스당 재생횟수 리스트 (장르: [index, N])
    
    
    # 1. 해시 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in genre_total_play:
            genre_total_play[genre] += play
            genre_index_play[genre].append([i, play])
        else:
            genre_total_play[genre] = play
            genre_index_play[genre] = [[i, play]]
            
    
    # 2. 많이 재생된 순으로 정렬
    # 많이 재생된 장르 정렬: items()로 key-value 쌍을 정렬
    sorted_genre_total_play = sorted(genre_total_play.items(), key=lambda item: item[1], reverse=True) 
    
    for genre, total_play in sorted_genre_total_play:
        # key genre에 해당하는 value(인덱스, 횟수)들을 정렬
        sorted_genre_index_play = sorted(genre_index_play[genre], key=lambda item: item[1], reverse=True) 
        
        # 최대 장르 개수 2만큼만 answer에 삽입
        genre_count = 0
        for i, play in sorted_genre_index_play:
            if genre_count >= 2:
                break
            answer.append(i)
            genre_count += 1    
                
    return answer
