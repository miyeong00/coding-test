def solution(answers):
    score = [0, 0, 0] # 수포자들이 맞힌 문제 수
    
    rule_first = [1, 2, 3, 4, 5] # 1번 수포자가 찍는 방식
    rule_second = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자가 찍는 방식
    rule_third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자가 찍는 방식
    
    for i in range(len(answers)):
        idx_first = i % len(rule_first)
        idx_second = i % len(rule_second)
        idx_third = i % len(rule_third)
        
        if answers[i] == rule_first[idx_first]:
            score[0] += 1
        if answers[i] == rule_second[idx_second]:
            score[1] += 1
        if answers[i] == rule_third[idx_third]:
            score[2] += 1
            
    answer = []
    
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
            
    return answer
            
    
    