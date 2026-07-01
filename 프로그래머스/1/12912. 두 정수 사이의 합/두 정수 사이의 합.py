def solution(a, b):
    num_list = []
    
    if a == b:
        return a
    elif a < b:
        for n in range(a, b+1):
            num_list.append(n)
        return sum(num_list)
    else:
        for n in range(b, a+1):
            num_list.append(n)
        return sum(num_list)
            