def solution(k, score):
    fame = [] # 명예의 전당
    answer = [] # 발표 점수
    for i in range(len(score)):
        if len(fame) < k:
            fame.append(score[i])
            fame.sort()
            answer.append(fame[0])
        else:
            if (score[i] >= max(fame)) or (max(fame) >= score[i] >= min(fame)):
                fame.remove(min(fame))
                fame.append(score[i])
                fame.sort()
                answer.append(fame[0])
            else:
                answer.append(fame[0])
    return answer