def solution(n, m, section):
    answer = 0
    painted_last = 0
    
    for s in section:
        if s > painted_last:
            answer += 1
            
            painted_last = s + m - 1
            
    return answer