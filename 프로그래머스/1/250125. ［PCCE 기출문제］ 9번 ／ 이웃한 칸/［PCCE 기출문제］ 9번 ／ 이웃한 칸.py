def solution(board, h, w):
    n = len(board)
    answer = 0 # board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if 0 <= nh < n and 0 <= nw < n:
            if board[h][w] == board[nh][nw]:
                answer += 1
    
    return answer