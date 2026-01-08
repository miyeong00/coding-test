def solution(dartResult):
    scores = [] # 점수들을 차례대로 담을 리스트
    
    # 1. 10점을 처리하기 편하게 바꿉니다 (예: '10' -> 'K')
    dartResult = dartResult.replace('10', 'K')
    
    for dart in dartResult:
        if dart.isdigit() or dart == 'K':
            # 2. 숫자(또는 K)라면 점수로 리스트에 추가
            if dart == 'K':
                scores.append(10)
            else:
                scores.append(int(dart))
                
        elif dart == 'S': # 1제곱 (그대로니까 할 일 없음)
            pass
        elif dart == 'D': # 2제곱 (가장 최근 점수 꺼내서 수정)
            scores[-1] = scores[-1] ** 2
        elif dart == 'T': # 3제곱
            scores[-1] = scores[-1] ** 3
            
        elif dart == '*': # 스타상: 현재와 이전 점수 모두 2배
            scores[-1] *= 2 # 현재 점수
            if len(scores) > 1: # 이전 점수가 있다면
                scores[-2] *= 2
                
        elif dart == '#': # 아차상: 현재 점수 마이너스
            scores[-1] *= -1
            
    # 모든 계산이 끝난 리스트의 합을 리턴
    return sum(scores)