def solution(n,a,b):
    answer = 0 # A번 참가자와 B번 참가자가 만나는 라운드의 횟수
    
    while (a != b):
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
        
    return answer
    