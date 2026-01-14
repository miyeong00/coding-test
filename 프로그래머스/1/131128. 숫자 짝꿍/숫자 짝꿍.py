def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        char_i = str(i)
        count = min(X.count(char_i), Y.count(char_i))
        answer += char_i * count
        
    if answer == '':
        return "-1"
    
    if answer[0] == '0':
        return "0"
    
    return answer