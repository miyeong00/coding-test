# 탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어감.
# 터널끼리 연결되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수 계산
# 탈주범은 시간당 1의 거리를 움직일 수 있음.
# 1 : 상하좌우 / 2 : 상하 / 3 : 좌우 / 4 : 상우
# 5 : 하우 / 6 : 하좌 / 7 : 상좌

from collections import deque

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # (너가 만든 테이블은 남겨둠 - 실제 이동은 dirs로 할게)
    dx = [[0, 0, 0, 0], [-1, 1, 0, 0], [-1, 1, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
    dy = [[0, 0, 0, 0], [0, 0, -1, 1], [0, 0, 0, 0], [0, 0, -1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, -1, 0]]

    # 방향 인덱스 통일: 0상 1하 2좌 3우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    opp = [1, 0, 3, 2]  # 반대방향(상<->하, 좌<->우)

    # 터널 타입별로 나갈 수 있는 방향
    dirs = {
        1: [0, 1, 2, 3],
        2: [0, 1],
        3: [2, 3],
        4: [0, 3],
        5: [1, 3],
        6: [1, 2],
        7: [0, 2],
    }

    start = board[R][C]
    answer = 0

    # 시작점이 0이면 갈 곳이 없음
    if start == 0:
        print(f"#{test_case} 0")
        continue

    visited = [[0] * M for _ in range(N)]  # 방문 시간(1부터)
    q = deque()

    visited[R][C] = 1
    q.append((R, C))
    answer = 1  # 시작점 포함

    while q:
        r, c = q.popleft()
        t = visited[r][c]
        if t == L:  # L시간이면 더 확장 X
            continue

        cur_type = board[r][c]
        for d in dirs[cur_type]:
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] != 0:
                continue
            nxt_type = board[nr][nc]
            if nxt_type == 0:
                continue

            # 다음 칸이 반대 방향으로 "들어오는" 통로가 있어야 연결됨
            if opp[d] in dirs[nxt_type]:
                visited[nr][nc] = t + 1
                q.append((nr, nc))
                answer += 1

    print(f"#{test_case} {answer}")



