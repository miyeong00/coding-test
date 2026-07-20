def solution(numbers):
    lst = []
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            lst.append(numbers[i] + numbers[j])
            
    answer = sorted(set(lst))
    
    return answer