# 방향 전환 테이블 
turn = [
    [],
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [3, 2, 0, 1],
    [2, 0, 3, 1],
    [2, 3, 0, 1]
]

dx = [-1, 0, 1, 0] # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

T_raw = input().strip()
if T_raw:
    T = int(T_raw)
    for test_case in range(1, T + 1):
        N = int(input())
        
        # 1. 벽을 5번 블록으로 감싸기
        # 보드를 (N+2)x(N+2) 크기로 만들고 테두리를 5로 채웁니다.
        board = [[5] * (N + 2)]
        for _ in range(N):
            board.append([5] + list(map(int, input().split())) + [5])
        board.append([5] * (N + 2))

        wormhole = [[] for _ in range(11)]
        starts = []

        # 패딩된 보드에서 시작점과 웜홀 위치 찾기
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                v = board[i][j]
                if v == 0:
                    starts.append((i, j))
                elif 6 <= v <= 10:
                    wormhole[v].append((i, j))

        answer = 0

        for sr, sc in starts:
            for sd in range(4):
                r, c = sr, sc
                d = sd
                score = 0

                while True:
                    # 다음 위치 계산
                    nr = r + dx[d]
                    nc = c + dy[d]

                    # 2. 종료 조건 확인: 다음 칸이 시작점이거나 블랙홀인 경우
                    if (nr, nc) == (sr, sc) or board[nr][nc] == -1:
                        break

                    # 3. 벽 체크가 필요 없음 (이미 5번 블록으로 감싸져 있음)
                    cell = board[nr][nc]

                    if cell == 0:
                        # 빈 공간이면 이동
                        r, c = nr, nc
                    elif 1 <= cell <= 5:
                        # 블록을 만나면 점수 추가 및 방향 전환 후 이동
                        score += 1
                        d = turn[cell][d]
                        r, c = nr, nc
                    elif 6 <= cell <= 10:
                        # 웜홀을 만나면 반대편 웜홀로 순간이동 (방향 유지)
                        wh_list = wormhole[cell]
                        if (nr, nc) == wh_list[0]:
                            r, c = wh_list[1]
                        else:
                            r, c = wh_list[0]
                    
                if score > answer:
                    answer = score

        print(f"#{test_case} {answer}")