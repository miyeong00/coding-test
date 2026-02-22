# 등산로를 만들기 위한 부지 : N x N 크기
# 등산로는 가장 높은 봉우리에서 시작해야 함.
# 등산로는 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 함.
# 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능
# 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있음.
# 만들 수 있는 가장 긴 등산로 찾기
# 지도에서 가장 높은 봉우리는 최대 5개
# 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def dfs(x, y, used, length):
    global answer

    answer = max(answer, length)
    cur_h = maps[x][y] # 현재 위치 높이

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue

        nh = maps[nx][ny]

        # 그냥 내려갈 수 있으면 이동
        if nh < cur_h:
            visited[nx][ny] = True
            dfs(nx, ny, used, length+1)
            visited[nx][ny] = False

        # 아직 공사 안 했고, 깎아서 내려갈 수 있으면 깎고 이동
        elif not used:
            work = nh - (cur_h - 1) # cur_h-1까지 깎기 위해 필요한 깊이
            if 1 <= work <= K:
                original = maps[nx][ny]
                maps[nx][ny] = cur_h - 1 # 깎기
                visited[nx][ny] = True
                dfs(nx, ny, True, length+1)
                visited[nx][ny] = False
                maps[nx][ny] = original # 복구

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N : 부지 크기, K : 최대 공사 가능 깊이
    maps = [list(map(int, input().split())) for _ in range(N)] # 지도 정보

    max_peak = 0
    for m in maps:
        for p in m:
            max_peak = max(p, max_peak)

    starts = [] # 가장 높은 봉우리들 좌표 => 시작점
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_peak:
                starts.append([i, j])

    answer = 0 # 가장 긴 등산로
    visited = [[False] * N for _ in range(N)] # 방문 여부 확인

    for sx, sy in starts:
        visited[sx][sy] = True
        dfs(sx, sy, False, 1)
        visited[sx][sy] = False

    print(f'#{test_case} {answer}')
