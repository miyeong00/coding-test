def solution(n):
    str = '수박'
    
    if n % 2 == 0:
        return str * (n//2)
    else:
        return str * (n//2) + '수'