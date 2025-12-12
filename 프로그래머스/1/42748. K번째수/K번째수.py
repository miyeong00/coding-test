def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        lst = array[start:end]
        lst.sort()
        answer.append(lst[commands[i][2] - 1])
        
    return answer
            