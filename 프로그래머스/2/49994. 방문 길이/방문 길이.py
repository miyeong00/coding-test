def solution(dirs):
    x = 0
    y = 0
    visited = set()
    answer = 0
    
    directions = {
        'U' : (0, 1),
        'D' : (0, -1),
        'R' : (1, 0),
        'L' : (-1, 0)
    }
    
    for dir in dirs:
        dx, dy = directions[dir]
        
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if ((x, y), (nx, ny)) not in visited:
                answer += 1
                visited.add(((x, y), (nx, ny)))
                visited.add(((nx, ny), (x, y)))
            x = nx
            y = ny
        else:
            continue
            
    return answer
        
        
            