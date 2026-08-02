def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0]
        end = command[1]
        order = command[2]
        
        arr = array[start - 1 : end]
        arr.sort()
        answer.append(arr[order - 1])
    
    return answer
            