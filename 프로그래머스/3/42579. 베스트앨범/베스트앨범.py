# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 출시
# 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르 내에서 많이 재생된 노래를 먼저 수록
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
# genres : 노래의 장르를 나타내는 문자열 배열
# plays : 노래별 재생 횟수를 나타내는 정수 배열
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 출력 

def solution(genres, plays):
    answer = []
    
    genre_count = {} # 장르별 재생 횟수
    for i in range(len(genres)):
        if genres[i] in genre_count:
            genre_count[genres[i]] += plays[i]
        else:
            genre_count[genres[i]] = plays[i]
            
    sorted_genres = sorted(genre_count, key=genre_count.get, reverse=True)
    
    genre_songs = {} # 장르별 노래 목록
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_songs:
            genre_songs[genre] = []
        
        genre_songs[genre].append((i, play))
        
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda song: (-song[1], song[0]))
        for song in sorted_songs[:2]:
            answer.append(song[0])
        
    return answer