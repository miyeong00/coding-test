def solution(d, budget):
    d_sorted = sorted(d)
    n = 0 # 지금까지 지원한 부서의 수
    
    for i in range(len(d_sorted)):
        if budget >= d_sorted[i]:
            budget -= d_sorted[i]
            n += 1
        else:
            break
            
    return n