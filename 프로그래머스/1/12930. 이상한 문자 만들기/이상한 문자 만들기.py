def solution(s):
    answer = ''
    
    n = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            n = 0
        else:
            if n % 2 == 0:
                answer += s[i].upper()
                n += 1
            else:
                answer += s[i].lower()
                n += 1
    return answer