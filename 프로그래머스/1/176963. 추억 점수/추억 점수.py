def solution(name, yearning, photo):
    answer = []
    for p in photo:
        score = 0
        for n in p:
            if n in name:
                idx = name.index(n)
                score += yearning[idx]
            else:
                score += 0
        answer.append(score)
        
    return answer