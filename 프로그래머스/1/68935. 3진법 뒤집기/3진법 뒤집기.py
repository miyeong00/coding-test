def solution(n):
    tenary = [] # 3진법 역순
    while n > 2:
        tenary.append(str(n%3))
        n //= 3
    tenary.append(str(n))
    tenary.reverse()
    
    answer = 0
    for i in range(len(tenary)):
        answer += int(tenary[i]) * (3 ** i)
    
    return answer