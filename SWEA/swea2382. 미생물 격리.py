# 정사각형 구역 안에 K개의 미생물 군집이 있음.
# N * N 개의 동일한 크기의 정사각형 셀
# 미생물들이 구역을 벗어나는 걸 방지하기 위해, 가장 바깥쪽 가장자리 부분에 위치한 셀들에는 특수한 약품이 칠해져 있음.
# 최초 각 미생물 군집의 위치와 군집 내 미생물의 수, 이동 방향이 주어짐.
# 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동
# 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀜.
# 미생물 수가 홀수인 경우, 살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림한 값
# 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 됨.
# 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 됨.
# M시간 동안 이 미생물 군집들을 격리함. M시간 후 남아 있는 미생물 수의 총합 구하기
# 상 : 1, 하 : 2, 좌 : 3, 우 : 4

import copy

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N : 구역의 한 변에 있는 셀의 개수, M : 격리 시간, K : 미생물 군집의 개수
    microorganism = [list(map(int, input().split())) for _ in range(K)] # 세로 위치, 가로 위치, 미생물 수, 이동 방향

    # 방향 : 상, 하, 좌, 우
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    # 반대 방향
    rev = [0, 2, 1, 4, 3]

    t = 0 # 시간
    square = [[[0, 0] for _ in range(N)] for _ in range(N)] # N * N 개의 동일한 크기의 정사각형 셀, 여기에 K개의 미생물 군집이 있음. [미생물 개수, 방향]

    new_microorganism = copy.deepcopy(microorganism) # 1시간 지난 후의 미생물 군집 현황

    # M시간 동안 반복
    while t < M:
        t += 1 # 1시간 증가

        temp = {} # key : (nr, nc) -> [sum_m, max_m, dir_of_max]

        # r : 세로 위치, c : 가로 위치, m : 미생물 수, d : 이동 방향
        for r, c, m, d in new_microorganism:
            nr = r + dx[d] # 현재 세로 위치
            nc = c + dy[d] # 현재 가로 위치

            # 약품이 칠해진 셀에 도착했을 경우
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                m = int(m // 2)
                d = rev[d]
                if m == 0:
                    continue # 다 죽으면 군집 제거

            # 갔는데 미생물이 있을 경우 (겹치는 경우)
            key = (nr, nc)
            if key not in temp:
                temp[key] = [m, m, d] # sum, max, dir
            else:
                temp[key][0] += m # sum 누적
                if m > temp[key][1]: # max 갱신되면 방향 갱신
                    temp[key][1] = m
                    temp[key][2] = d

        # 다음 시간 군집 리스트 초기화
        new_microorganism = []
        for (r, c), (sum_m, max_m, dir_max) in temp.items():
            new_microorganism.append([r, c, sum_m, dir_max])
    
    # M시간 후 총합
    answer = 0
    for r, c, m, d in new_microorganism:
        answer += m
                    
    print(f'#{test_case} {answer}')

