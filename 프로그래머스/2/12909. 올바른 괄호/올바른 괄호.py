def solution(s):
    stack = [] # 스택
    
    for p in s:
        if len(stack) == 0:
            stack.append(p)
        else:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
                
    if len(stack) == 0:
        return True
    else:
        return False