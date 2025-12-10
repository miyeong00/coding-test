def solution(s):
    answer = []
    
    for i in range(len(s)):
        if s[i] in s[:i]:
            all_index = list(filter(lambda x: s[x] == s[i], range(i)))
            answer.append(i - all_index[-1])
        else:
            answer.append(-1)
        
    return answer