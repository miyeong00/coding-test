T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 달팽이 크기
    grid = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1] # 행 변화량
    dy = [1, 0, -1, 0] # 열 변화량
    dist = 0 # 현재 방향 (0:우, 1:하, 2:좌, 3:상)
    x, y = 0, 0 # 현재 위치
    
    for num in range(1, N*N+1):
        grid[x][y] = num

        nx = x + dx[dist]
        ny = y + dy[dist]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] != 0:
            dist = (dist + 1) % 4
            x = x + dx[dist]
            y = y + dy[dist]
        else:
            x = nx
            y = ny

    print(f'#{test_case}')
    for row in grid:
        print(*row)