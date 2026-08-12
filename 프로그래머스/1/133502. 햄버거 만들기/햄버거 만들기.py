# 빵(1) - 야채(2) - 고기(3) - 빵(1) 
# ingredient : 상수에게 전해지는 재료의 정보를 나타내는 정수 배열
# 상수가 포장하는 햄버거의 개수 출력

def solution(ingredient):
    answer = 0 # 상수가 포장하는 햄버거의 개수 
    stack = [] # 햄버거 재료 쌓는 스택
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                for i in range(4):
                    stack.pop()
                answer += 1
                
    return answer
