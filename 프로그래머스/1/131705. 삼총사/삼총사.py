# 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 함.
# number : 학생들의 번호를 나타내는 정수 배열
# 학생들 중 삼총사를 만들 수 있는 방법의 수 출력

def solution(number):
    answer = 0 # 삼총사를 만들 수 있는 방법의 수
    
    # 삼총사 만들기
    # idx : 지금 몇 번째 학생을 보고 있는지
    # count : 지금까지 몇 명을 뽑았는지
    # total : 뽑은 학생 번호의 합 
    def triple(idx, count, total):
        nonlocal answer

        # 학생 3명을 모두 뽑은 경우
        if count == 3:
            if total == 0:
                answer += 1
            return

        # 더 볼 학생이 없으면 종료 
        if idx == len(number):
            return
        
        # 1. 현재 학생을 뽑는 경우
        triple(idx + 1, count + 1, total + number[idx])
        
        # 2. 현재 학생을 뽑지 않는 경우
        triple(idx + 1, count, total)
    
    triple(0, 0, 0)
    
    return answer