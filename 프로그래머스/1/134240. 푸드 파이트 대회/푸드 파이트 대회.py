def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    
    answer_2 = ''
    for i in range(len(answer)-1,-1,-1):
        answer_2 += answer[i]
        
    return answer + str(0) + answer_2