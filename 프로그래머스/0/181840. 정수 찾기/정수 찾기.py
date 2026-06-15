def solution(num_list, n):
    answer = 0
    
    for num in num_list:
        if num == n:
            answer += 1
        else:
            pass
        
    if answer >= 1:
        return 1
    else:
        return 0