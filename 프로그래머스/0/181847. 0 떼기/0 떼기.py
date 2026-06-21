def solution(n_str):
    str_i = 0 # 0이 아닌 숫자의 첫 인덱스
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            str_i = i
            break
            
    if str_i >= 1:
        return n_str[str_i:]
    else:
        return n_str
            