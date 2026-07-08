# numbers : 사용할 수 있는 숫자가 담긴 배열
# target : 타겟 넘버
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수 구하기 
def solution(numbers, target):
    answer = 0
    
    def make_target(idx, total):
        nonlocal answer
        
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        make_target(idx + 1, total + numbers[idx])
        
        make_target(idx + 1, total - numbers[idx])
    
    make_target(0, 0)
        
    return answer