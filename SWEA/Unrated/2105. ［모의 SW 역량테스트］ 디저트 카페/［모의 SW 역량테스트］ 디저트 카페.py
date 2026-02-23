# 한 변의 길이가 N인 정사각형 모양을 가진 지역에 디저트 카페가 모여 있음.
# 원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류
# 카페들 사이에는 대각선 방향으로 움직일 수 있는 길들이 있음.
# 디저트 카페 투어는 어느 한 카페에서 출발하여 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 함.
# 디저트 카페 투어를 하는 도중 해당 지역을 벗어나면 안 됨.
# 카페 투어 중 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 됨.
# 하나의 카페에서 디저트를 먹는 것도 안 됨.
# 왔던 길을 다시 돌아가는 것도 안 됨.
# 디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력
# 디저트를 먹을 수 없는 경우 -1 출력

# 대각선 방향 (왼쪽 아래에서부터 시작해서 시계 방향)
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

# x, y : 현재 위치 좌표, d : 현재 방향, lenght : 지금까지 먹은 디저트 개수, (sx, sy) : 시작 위치
def dfs(x, y, d, length, sx, sy):
    global answer

    # 다음 이동 후보 : 같은 방향 유지, 또는 다음 방향으로 꺾기
    for nd in (d, d + 1):
        if nd >= 4:
            continue

        nx = x + dx[nd]
        ny = y + dy[nd]

        # 범위 체크
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        # 시작점으로 복귀하는 경우(성공 조건)
        if nx == sx and ny == sy:
            # 최소 4개 이상 + 마지막 방향까지 써서 사각형 형태가 되었을 때만 인정
            if nd == 3 and length >= 4:
                answer = max(length, answer)
            continue

        # 디저트 중복 체크
        dessert = board[nx][ny]
        if dessert_used[dessert]:
            continue

        # 방문 체크
        if visited[nx][ny]:
            continue

        # 선택
        dessert_used[dessert] = True
        visited[nx][ny] = True

        dfs(nx, ny, nd, length+1, sx, sy)

        # 복구
        visited[nx][ny] = False
        dessert_used[dessert] = False

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 디저트 카페 지역의 한 변의 길이
    board = [list(map(int, input().split())) for _ in range(N)] # 디저트 종류에 대한 정보

    answer = -1 # 가장 많이 먹을 수 있는 디저트의 수
    dessert_used = [False] * 101 # 디저트 번호 1 ~ 100
    visited = [[False] * N for _ in range(N)] # 방문 여부 확인

    for i in range(N):
        for j in range(N):
            # 시작점 세팅
            dessert_used[board[i][j]] = True
            visited[i][j] = True

            dfs(i, j, 0, 1, i, j)

            visited[i][j] = False
            dessert_used[board[i][j]] = False

    print(f'#{test_case} {answer}')
