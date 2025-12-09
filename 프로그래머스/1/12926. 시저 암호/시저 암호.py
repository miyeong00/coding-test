def solution(s, n):
    alphabet_upper = ['A','B','C','D','E','F','G','H',
                      'I','J','K','L','M','N','O','P',
                      'Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_lower = ['a','b','c','d','e','f','g','h',
                      'i','j','k','l','m','n', 'o','p','q','r','s',
                      't','u','v','w','x','y','z']
             
    answer = ''
    for i in range(len(s)):
         if s[i] == ' ':
            answer += ' '
         else:
            if s[i] in alphabet_upper:
                idx = alphabet_upper.index(s[i])
                if idx + n >= 26:
                    answer += alphabet_upper[idx + n - 26]
                else:
                    answer += alphabet_upper[idx + n]
            elif s[i] in alphabet_lower:
                idx = alphabet_lower.index(s[i])
                if idx + n >= 26:
                    answer += alphabet_lower[idx + n - 26]
                else:
                    answer += alphabet_lower[idx + n]
                    
    return answer