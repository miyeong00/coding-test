def solution(k, m, score):
    answer = 0
    sorted_score = sorted(score, reverse=True)
    
    for i in range(m-1, len(score), m):
        answer += sorted_score[i] * m
    
    return answer