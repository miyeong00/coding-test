# 줄기세포들을 배양 용기에 도포한 후 일정 시간 동안 배양을 시킨 후 줄기 세포의 개수가 몇 개가 되는지 계산
# 하나의 줄기 세포는 가로, 세로 크기가 1인 정사각형 형태로 존재
# 배양 용기는 격자 그리드로 구성되어 있음.
# 초기 상태에서 줄기 세포들은 비활성 상태이며 생명력 수치가 X인 줄기 세포의 경우 X시간 동안 비활성 상태
# X시간이 지나는 순간 활성 상태가 됨.
# 세포가 죽더라도 소멸되는 것은 아니고 죽은 상태로 해당 그리드 셀을 차지하게 됨.
# 활성화된 줄기 세포는 첫 1시간 동안 상, 하, 좌, 우 네 방향으로 동시에 번식함.
# 번식된 줄기 세포는 비활성 상태
# 하나의 그리드 셀에는 하나의 줄기 세포만 존재할 수 있기 때문에 번식하는 방향에 이미 줄기 세포가 존재하는 경우 해당 방향으로 추가적으로 번식하지 않음.
# 두 개 이상의 줄기 세포가 하나의 그리드 셀에 동시 번식하려고 하는 경우 생명력 수치가 높은 줄기 세포가 해당 그리드 셀을 혼자서 차지하게 됨.
# 줄기 세포의 초기 상태 정보와 배양 시간 K시간이 주어질 때, K시간 후 살아있는 줄기 세포(비활성 상태 + 활성 상태)의 총 개수 구하기
# 1~10 : 해당 그리드 셀에 위치한 줄기 세포의 생명력
# 0 : 줄기 세포가 존재하지 않는 그리드
# 1 <= 배양 시간 K <= 300
# 1 <= 줄기 세포의 생명력 X <= 10

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # cells[(r, c)] = [life, status_time, state]
    # state: 0(비활성), 1(활성), 2(죽음)
    # status_time: 해당 상태에서 경과한 시간
    cells = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0:
                # [생명력, 현재 상태 유지 시간, 상태(0:비활성)]
                cells[(i, j)] = [grid[i][j], 0, 0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(K):
        new_cells = {}  # 이번 시간에 번식되어 새로 생길 후보들
        
        # 현재 존재하는 모든 세포 순회 (딕셔너리 아이템 복사본 사용)
        for pos, info in cells.items():
            life, time, state = info
            
            # 1. 상태 변화 및 번식 로직
            if state == 0:  # 비활성 상태
                if time + 1 == life:
                    cells[pos][2] = 1  # 활성으로 변경
                    cells[pos][1] = 0  # 시간 초기화
                else:
                    cells[pos][1] += 1
            
            elif state == 1:  # 활성 상태
                # 활성화된 '첫 1시간' 동안만 번식
                if time == 0:
                    r, c = pos
                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]
                        if (nr, nc) not in cells and (nr, nc) not in new_cells:
                            new_cells[(nr, nc)] = life
                        elif (nr, nc) in new_cells:
                            # 이미 이번 타임에 번식 후보라면 생명력 비교
                            if new_cells[(nr, nc)] < life:
                                new_cells[(nr, nc)] = life
                
                # 활성 시간 카운트 및 죽음 처리
                if time + 1 == life:
                    cells[pos][2] = 2  # 죽음
                    cells[pos][1] = 0
                else:
                    cells[pos][1] += 1
            
            # 죽은 상태(state 2)는 아무것도 하지 않음 (공간만 차지)

        # 2. 번식 후보들을 실제 세포 딕셔너리에 추가
        for pos, life in new_cells.items():
            cells[pos] = [life, 0, 0]

    # 살아있는 세포 (비활성 + 활성) 카운트
    answer = sum(1 for info in cells.values() if info[2] < 2)
    print(f"#{test_case} {answer}")