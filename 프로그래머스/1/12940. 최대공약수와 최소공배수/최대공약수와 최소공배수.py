def solution(n, m):
    answer = []
    original_n = n
    original_m = m
    
    min_num = min(n, m)
    
    # 최대공약수
    while min_num > 0:
        if n % min_num == 0 and m % min_num == 0:
            answer.append(min_num)
            break
        else:
            min_num -= 1
            
    # 최소공배수
    lcm_val = (n * m) // answer[0]
    answer.append(lcm_val)
    
    return answer