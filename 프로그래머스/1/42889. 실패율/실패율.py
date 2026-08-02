# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# N : 전체 스테이지 개수
# stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 출력 

def solution(N, stages):
    count = [0] * (N + 2)
    
    for s in stages:
        count[s] += 1
        
    total = len(stages)
    failure = []
    
    for i in range(1, N + 1):
        if total == 0:
            rate = 0
        else:
            rate = count[i] / total
        failure.append((i, rate))
        total -= count[i]
        
    failure.sort(key=lambda x: x[1], reverse=True)
    answer = [stage for stage, rate in failure]
        
    return answer
    