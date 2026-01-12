def solution(n, lost, reserve):
    answer = 0 # 체육수업을 들을 수 있는 학생의 최댓값
    clothes = [1] * n # 학생들의 체육복 수
    
    for r in reserve:
        clothes[r-1] += 1
    
    for l in lost:
        clothes[l-1] -= 1
        
    for i in range(len(clothes)):
        if clothes[i] == 0:
            if i > 0 and clothes[i-1] >= 2:
                clothes[i-1] -= 1
                clothes[i] += 1
            elif i < n-1 and clothes[i+1] >= 2:
                clothes[i+1] -= 1
                clothes[i] += 1
                
    for cloth in clothes:
        if cloth >= 1:
            answer += 1
            
    return answer