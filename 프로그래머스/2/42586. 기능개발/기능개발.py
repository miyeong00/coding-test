# 각 기능은 진도가 100%일 때 서비스에 반영 가능
# 뒤에 있는 게 앞에 있는 거보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 건 앞에 있는 게 배포될 때 함께 배포됨.
# progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
# speeds : 각 작업의 개발 속도가 적힌 정수 배열
# 각 배포마다 몇 개의 기능이 배포되는지 출력

def solution(progresses, speeds):
    days = [] # 각 기능들이 배포될 때까지 며칠 걸리는지
    answer = [] # 각 배포마다 몇 개의 기능이 배포되는지 출력
    
    for i in range(len(speeds)):
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            days.append(remain // speeds[i])
        else:
            days.append(remain // speeds[i] + 1)
    
    i = 0
    while i < len(days):
        standard = days[i]
        i += 1
        count = 1
        
        while i < len(days) and standard >= days[i]:
            i += 1
            count += 1
        
        answer.append(count)
        
    return answer
            
            
    
        
        
            
    