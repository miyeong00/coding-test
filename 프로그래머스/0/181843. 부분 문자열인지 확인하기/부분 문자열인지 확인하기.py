def solution(my_string, target):
    answer = 0
    
    n_tg = len(target) # target의 길이
    
    comp = '' # 비교할 문자열
    
    for i in range(len(my_string) - n_tg + 1):
        comp = my_string[i:(i+n_tg)]
        
        if comp == target:
            answer += 1
    
    if answer >= 1:
        return 1
    else:
        return 0