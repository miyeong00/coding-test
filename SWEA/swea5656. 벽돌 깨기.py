# 구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 W x H 배열로 주어짐.
# 0은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미
# 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있음.
# 벽돌은 숫자 1 ~ 9로 표현되며, 구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1)칸만큼 같이 제거됨.
# N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 할 때, 남은 벽돌의 개수 구하기

from collections import deque

# 열에서 맨 위 벽돌 찾기
def first_brick(board, col, H):
    for row in range(H):
        if board[row][col] != 0:
            return row
    return -1

# 폭발
def explode(board, row, col, H, W):
    dr = [-1, 1, 0, 0] # 상하좌우, row
    dc = [0, 0, -1, 1] # 상하좌우, col
    q = deque() # 터지는 벽돌 큐

    power = board[row][col] # 시작 벽돌
    q.append((row, col, power))
    board[row][col] = 0 # 시작칸 바로 0으로 만들기

    while q:
        r, c, p = q.popleft()

        for d in range(4):
            for step in range(1, p):
                nr = r + dr[d] * step
                nc = c + dc[d] * step

                if 0 <= nr < H and 0 <= nc < W:
                    if board[nr][nc] == 0:
                        continue
                    else:
                        np = board[nr][nc]
                        q.append((nr, nc, np))
                        board[nr][nc] = 0
                else:
                    break

# 중력
def gravity(board, H, W):
    for col in range(W):
        stack = []
        for row in range(H-1, -1, -1):
            if board[row][col] != 0:
                stack.append(board[row][col])
        
        row = H - 1
        for val in stack:
            board[row][col] = val
            row -= 1

        for rr in range(row, -1, -1):
            board[rr][col] = 0

# 한 번 샷 적용
def apply_shot(board, col, H, W):
    row = first_brick(board, col, H)
    
    if row == -1:
        return board
    
    explode(board, row, col, H, W)
    gravity(board, H, W)
    
    return board

def count_bricks(board, H, W):
    count = 0

    for row in range(H):
        for col in range(W):
            if board[row][col] != 0:
                count += 1
    return count

def dfs(cnt, board, N, H, W):
    global answer

    remain = count_bricks(board, H, W)

    if remain == 0:
        answer = 0
        return
    
    if cnt == N:
        answer = min(answer, remain)
        return
    
    for col in range(W):
        new_board = [row[:] for row in board] 
        apply_shot(new_board, col, H, W)
        dfs(cnt + 1, new_board, N, H, W)
    

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, W, H = map(int, input().split()) # N : 구슬의 개수, W : 배열의 가로, H : 배열의 세로
    bricks = [list(map(int, input().split())) for _ in range(H)] # 벽돌들의 정보

    answer = count_bricks(bricks, H, W)
    dfs(0, bricks, N, H, W)
    print(f'#{test_case} {answer}')

