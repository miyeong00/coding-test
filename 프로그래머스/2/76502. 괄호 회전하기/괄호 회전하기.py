# s를 왼쪽으로 x칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수

def solution(s):
    answer = [] # x칸 되는 애들
    
    for i in range(len(s)):
        stack = [] # 올바른 괄호 문자열인지 확인하는 스택
        
        for j in range(i, i+len(s)):
            if len(stack) == 0:
                stack.append(s[j % len(s)])
            else:
                if s[j % len(s)] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        break
                elif s[j % len(s)] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        break
                elif s[j % len(s)] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        break
                else:
                    stack.append(s[j % len(s)])
                    
        if len(stack) == 0:
            answer.append(i)
            
    return len(answer)