def solution(wallpaper):
    answer = [50, 50, 0, 0]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if answer[0] > i:
                    answer[0] = i
                if answer[2] < i+1:
                    answer[2] = i+1
                if answer[1] > j:
                    answer[1] = j
                if answer[3] < j+1:
                    answer[3] = j+1
            
    return answer