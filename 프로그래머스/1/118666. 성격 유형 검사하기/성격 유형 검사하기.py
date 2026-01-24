def solution(survey, choices):
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scores = {t: 0 for t in types}
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    for i in range(len(choices)):
        choice = choices[i]
        if choice < 4: # 비동의 (앞 글자 유형)
            scores[survey[i][0]] += score_map[choice]
        elif choice > 4: # 동의 (뒷 글자 유형)
            scores[survey[i][1]] += score_map[choice]
            
    answer = ''
    if scores['R'] >= scores['T']: answer += 'R'
    else: answer += 'T'

    if scores['C'] >= scores['F']: answer += 'C'
    else: answer += 'F'
    
    if scores['J'] >= scores['M']: answer += 'J'
    else: answer += 'M'
    
    if scores['A'] >= scores['N']: answer += 'A'
    else: answer += 'N'
    
    return answer